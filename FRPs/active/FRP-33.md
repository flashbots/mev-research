---
id: 33
title: Attestation Stack for TEE-based Protocols
team: Andrew Miller (hbcl), Sylvain Bellemare (hbcl)
created: 2023-06-14
status: active
---

# `auditee`: Towards an Attestation Stack for TEE-based Protocols
<!--
Follow this template for new research proposals, removing this text and replacing the *Flashbots Research Proposal Template* title with your proposal's own. Open a pull request to submit your proposal, using an abbreviated title in the filename (`proposal-short_title.md`), and put the file under the `FRPs` folder.
-->
<!--
Use this initial section to provide a ~500 word summary of the proposal. The summary should consist in a simple straightforward statement of what your hypothesis is, what methodology you intend to use, what limitations those methods may have, what implications your results may have.
-->

## Background and Problem Statement
<!-- Provide motivation and background for the proposal, and clearly state the research questions it aims to tackle. Link to related or dependent Research Question(s) on the Flashbots Research Roadmap, and reference relevant Github Issues in this repository.-->
[`auditee`][auditee], as a starting point, aims at giving a single script that carries out
the entire end-to-end auditing task, including the reproducible build, as well as
verifying all intermediate signatures in the certificate chain. A more comprehensive
solution would provide data availability and a visible public repository for all of the
evidence associated with attestations. This is an ecosystem wide problem, since
TEE-based private smart contracts, non-blockchain TEE applications like Signal or
enterprise applications also do not do a thorough job at this. There is a need for an
orchestrator to elevate this playing field. Perhaps this could evolve as a dashboard.


## Plan and Deliverables
<!-- Describe the planned approach to the problem, including potential time allocations and partitioning into phases. List the artifacts or intended deliverables of the proposal. -->
### TEE reductions in Rust & Gramine-Python (FRP-A)
We are often interested in small self-contained enclaves that do a small task but are
amenable to software analysis. This can include small Python / Go programs using
Gramine, as well as low-level implementations via the Rust SGX SDK. The appeal of low
level implementations especially is that we have a better chance of carefully studying
and mitigating the side channels, i.e. to account for the side channels we have to
tolerate, and to help check if a mitigation (constant time implementation) is working.

Since running EVM within an enclave is necessary anyway, the concrete proposal here is
to develop a small reproducible enclave that evaluates EVM directly in Rust SGX SDK,
and a Python demo in Gramine where the build is not guaranteed reproducible. We will
include a write-up to the forum summarizing the process involved in making this
reproducible package.

### Reproducible builds for Gramine-based enclaves (FRP-B)
If we really want to use Gramine in a production system, we should include
reproducible builds for Gramine itself. The [previous effort][reprobuilds-gramine-nix]
to do this via Nix packages didn't get the Gramine upstream authors to agree to support
it. What's left is the straightforward but tedious task of porting it ourselves as well
as tracking upstream patches. Nix is the basis of reproducible builds. So there's no
special knowledge needed to adapt Gramine to Nix, just need to systematically make a
Nix pinned build package for each dependency.

Don't know how to automate this better, but Gramine is bounded so this is estimated to
take about 1 month.  We will conclude this effort with a writeup to the forum explaining
the process in as clear detail as we can, in order to estimate the effort required to
continuously apply upstream Gramine patches.
([Early work-in-progress implementation of a nix flake for gramine.][gramine-flake_nix])

Part of this work could also help bringing more clarity about what it takes to support
reproducible builds. Different projects use different tools, and it's somehow
difficult to be certain whether the different tools do in fact achieve reproducible
builds over a reasonable span of time. In the context of enclave applications, it has
yet to be clarified how important reproducible builds are, and how far out in the future
should a given enclave binary should be reproducible from its source code. Currently,
multiple projects rely on docker images, and although this may work for a limited amount
of time, would this work for multiple months? This is not clear at all.

Some examples of projects where the topic of reproducible builds is still an open issue:

* [Rust SGX SDK][reprobuilds-rust_sgx_sdk]
* [Oasis Network][reprobuilds-oasis]
* [Secret Network][reprobuilds-secret]
* [Gramine][reprobuilds-gramine]
* [Flashbots Geth-in-SGX][reprobuilds-flashbots]

Is considered resolved with Nix:
* [Intel C++ SGX SDK][reprobuilds-cpp_sgx_sdk]
* [Intel architectural enclaves][reprobuilds-sgx-ae]

Is considered resolved via Docker:
* [Mobilecoin][reprobuilds-mobilecoin]
* [CosmWasm Rust Optimizer][reprobuilds-cosmwasm]


### Possible follow ups
#### Documentation and scaling up of the Reproducible Builds process
Right now it is a straightforward but tedious task, but the skill for doing it and
handling edge cases is not really portable either. Let's document this process so we can
at least outsource it more effectively? The next question is to pursue automation.

#### Verification of Quoting & Provisioning Enclaves (Architectural Enclaves)
In the context of Intel SGX, remote attestation relies on prebuilt
[architectural enclaves][sgx-ae]. Although the code of these enclaves is
[open source][sgx-ae-source], when deployed their binary form must be signed by Intel.
Thus, using SGX implies one is trusting Intel for their architectural enclaves as well
as their chips, etc. It's nevertheless possible to audit the code, and furthermore some
verification mechanism could perhaps be implemented such that combined with reproducible
builds, a remote attestation flow would somehow be verifiable such that the generated
quote would be proven to be from the expected quoting enclave. This verification flow
would also apply to custom enclaves that are used in [DCAP-based][dcap] attestation
flows.

#### Enclave Hub Prototype
To kickstart the discussion of how to orchestrate the Attestation Stack, and build
towards the vision of Enclave Transparency, a proposed starting point is Enclave Hub.
Basically this would be a dashboard website that provides data availability for all the
source code dependencies needed to rebuild the attestation stack.

## References
<!-- Reference current relevant literature or past work pertaining to the research question(s) at stake. -->
* [`auditee`][auditee]
* [Nix-based reproducible builds for Intel's C++ SGX SDK][reprobuilds-cpp_sgx_sdk]
* [Intel's nix-based tooling to verify the reproducibiliy of its architectural enclaves][reprobuilds-sgx-ae]
* [Open issue for reproducible builds for the Rust SGX SDK][reprobuilds-rust_sgx_sdk]
* [Open issue for reproducible builds for Oasis Protocol][reprobuilds-oasis]
* [Open issue for reproducible builds for Secret Network][reprobuilds-secret]
* [Open issue for reproducible builds for Gramine][reprobuilds-gramine]


[auditee]: https://auditee.readthedocs.io/en/latest/index.html
[reprobuilds-cpp_sgx_sdk]: https://github.com/NixOS/nixpkgs/pull/126990
[reprobuilds-rust_sgx_sdk]: https://github.com/apache/incubator-teaclave-sgx-sdk/issues/52
[reprobuilds-sgx]: https://github.com/intel/linux-sgx/tree/master/linux/reproducibility
[reprobuilds-sgx-ae]: https://github.com/intel/linux-sgx/tree/master/linux/reproducibility/ae_reproducibility_verifier
[reprobuilds-mobilecoin]: https://github.com/mobilecoinfoundation/mobilecoin/pull/1693#issuecomment-1150239428
[reprobuilds-oasis]: https://github.com/oasisprotocol/oasis-core/issues/2596
[reprobuilds-secret]: https://github.com/scrtlabs/SecretNetwork/issues/1467
[reprobuilds-gramine]: https://github.com/gramineproject/gramine/issues/153
[reprobuilds-gramine-nix]: https://github.com/gramineproject/gramine/issues/153#issuecomment-1489209009
[gramine-flake_nix]: https://github.com/sbellem/gramine/blob/1.4-nix/flake.nix
[reprobuilds-flashbots]: https://github.com/flashbots/geth-sgx-gramine/issues/8
[reprobuilds-cosmwasm]: https://github.com/CosmWasm/rust-optimizer
[dcap]: https://download.01.org/intel-sgx/latest/dcap-latest/linux/docs/DCAP_ECDSA_Orientation.pdf
[sgx-ae]: https://github.com/intel/linux-sgx/blob/master/linux/reproducibility/ae_reproducibility_verifier/reproducibility_verifier.sh#L43-L46
[sgx-ae-source]: https://github.com/intel/linux-sgx/tree/master/psw/ae

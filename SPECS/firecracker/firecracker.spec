# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           firecracker
Version:        1.17.0
Release:        %autorelease
Summary:        Lightweight virtual machine monitor
License:        Apache-2.0
URL:            https://firecracker-microvm.github.io/
VCS:            git:https://github.com/firecracker-microvm/firecracker
#!RemoteAsset:  sha256:1f61367c07266dc9caa5135d655ba532a3d6a994b9320eec85de5efcbd8a759f
Source0:        https://github.com/firecracker-microvm/firecracker/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:4daf05d0fff9f21c976db907a4cea4c4a4adda3f933d3a6a1840013c40c1eeb4
Source1:        https://github.com/firecracker-microvm/micro-http/archive/7975fe0e59000e8c41cb1d58fbd39ffa102e5b27.tar.gz#/micro-http-7975fe0e59000e8c41cb1d58fbd39ffa102e5b27.tar.gz
ExclusiveArch:  riscv64
BuildSystem:    rust

# Adapt the upstream experimental RISC-V backend to Firecracker 1.17.0.
# porting from ArchLinux: https://github.com/felixonmars/archriscv-packages/pull/6032
%ifarch riscv64
#!RemoteAsset:  sha256:9e2acd2def0dd2bebc3d5e068cb9a51c615da1a7bcf91338d92ce9e19611858a
Patch0:         0001-firecracker-riscv64.patch
%endif

# Replace the pinned Git dependency with the matching packaged source archive.
Patch2000:      2000-use-local-micro-http-source.patch

BuildRequires:  rust-rpm-macros
BuildRequires:  rust >= 1.97
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  binutils
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  perl
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  crate(anstream-1) >= 1.0.0
BuildRequires:  crate(anstyle-1) >= 1.0.14
BuildRequires:  crate(anstyle-parse-1) >= 1.0.0
BuildRequires:  crate(anstyle-query-1) >= 1.1.5
BuildRequires:  crate(alloca-0.4) >= 0.4.0
BuildRequires:  crate(arrayvec-0.7/default) >= 0.7.6
BuildRequires:  crate(annotate-snippets-0.11) >= 0.11.4
BuildRequires:  crate(aws-lc-rs-1) >= 1.18.2
BuildRequires:  crate(aws-lc-fips-sys-0.14) >= 0.14.2
BuildRequires:  crate(aws-lc-sys-0.46) >= 0.46.0
BuildRequires:  crate(base64-0.23) >= 0.23.1
BuildRequires:  crate(bindgen-0.69) >= 0.69.5
BuildRequires:  crate(bindgen-0.72) >= 0.72.0
BuildRequires:  crate(bindgen-0.73/default) >= 0.73.0
BuildRequires:  crate(bitcode-0.6) >= 0.6.9
BuildRequires:  crate(bitcode-derive-0.6) >= 0.6.9
BuildRequires:  crate(bitflags-1) >= 1.3.2
BuildRequires:  crate(bitflags-2) >= 2.13.1
BuildRequires:  crate(bitvec-1) >= 1.1.1
BuildRequires:  crate(bytemuck-1) >= 1.25.2
BuildRequires:  crate(byteorder-1) >= 1.5.0
BuildRequires:  crate(cc-1) >= 1.4.4
BuildRequires:  crate(cargo-toml-1) >= 1.0.0
BuildRequires:  crate(cexpr-0.6) >= 0.6.0
BuildRequires:  crate(cfg-if-1) >= 1.0.4
BuildRequires:  crate(chacha20-0.10) >= 0.10.2
BuildRequires:  crate(clang-sys-1) >= 1.9.1
BuildRequires:  crate(clap-4) >= 4.6.6
BuildRequires:  crate(clap-builder-4) >= 4.6.6
BuildRequires:  crate(clap-derive-4) >= 4.6.4
BuildRequires:  crate(clap-lex-1) >= 1.1.0
BuildRequires:  crate(clap-complete-4) >= 4.0.0
BuildRequires:  crate(clap-num-1) >= 1.2.0
BuildRequires:  crate(cmake-0.1) >= 0.1.58
BuildRequires:  crate(colorchoice-1) >= 1.0.5
BuildRequires:  crate(convert-case-0.10) >= 0.10.0
BuildRequires:  crate(criterion-0.8) >= 0.8.2
BuildRequires:  crate(criterion-plot-0.8/default) >= 0.8.2
BuildRequires:  crate(csv-1/default) >= 1.1.0
BuildRequires:  crate(crc64-2) >= 2.0.0
BuildRequires:  crate(derive-more-2) >= 2.1.1
BuildRequires:  crate(derive-more-impl-2) >= 2.1.1
BuildRequires:  crate(displaydoc-0.2) >= 0.2.7
BuildRequires:  crate(device-tree-1/default) >= 1.1.0
BuildRequires:  crate(dunce-1) >= 1.0.5
BuildRequires:  crate(either-1) >= 1.18.0
BuildRequires:  crate(env-logger-0.11/default) >= 0.11.10
BuildRequires:  crate(event-manager-0.4) >= 0.4.2
BuildRequires:  crate(find-msvc-tools-0.1) >= 0.1.11
BuildRequires:  crate(futures-0.3/executor) >= 0.3.0
BuildRequires:  crate(fs-extra-1) >= 1.3.0
BuildRequires:  crate(funty-2) >= 2.0.0
BuildRequires:  crate(getrandom-0.4) >= 0.4.3
BuildRequires:  crate(glam-0.21) >= 0.21.0
BuildRequires:  crate(glob-0.3) >= 0.3.4
BuildRequires:  crate(heck-0.5) >= 0.5.0
BuildRequires:  crate(is-terminal-polyfill-1) >= 1.70.2
BuildRequires:  crate(itertools-0.12) >= 0.12.1
BuildRequires:  crate(itertools-0.15/default) >= 0.15.0
BuildRequires:  crate(itoa-1) >= 1.0.18
BuildRequires:  crate(jobserver-0.1) >= 0.1.35
BuildRequires:  crate(kvm-bindings-0.14) >= 0.14.1
BuildRequires:  crate(kvm-ioctls-0.25) >= 0.25.0
BuildRequires:  crate(lazy-static-1) >= 1.5.0
BuildRequires:  crate(lazycell-1) >= 1.3.0
BuildRequires:  crate(libc-0.2) >= 0.2.189
BuildRequires:  crate(libloading-0.8) >= 0.8.9
BuildRequires:  crate(linux-loader-0.14) >= 0.14.0
BuildRequires:  crate(linux-raw-sys-0.12) >= 0.12.1
BuildRequires:  crate(log-0.4) >= 0.4.33
BuildRequires:  crate(memchr-2) >= 2.8.3
BuildRequires:  crate(memfd-0.6) >= 0.6.5
BuildRequires:  crate(minimal-lexical-0.2) >= 0.2.1
BuildRequires:  crate(nix-0.27) >= 0.27.1
BuildRequires:  crate(nom-7) >= 7.1.3
BuildRequires:  crate(pkg-config-0.3) >= 0.3.34
BuildRequires:  crate(proc-macro2-1) >= 1.0.107
BuildRequires:  crate(quote-1) >= 1.0.47
BuildRequires:  crate(page-size-0.6/default) >= 0.6.0
BuildRequires:  crate(plotters-0.3/area-series) >= 0.3.2
BuildRequires:  crate(plotters-0.3/line-series) >= 0.3.2
BuildRequires:  crate(plotters-0.3/svg-backend) >= 0.3.2
BuildRequires:  crate(radium-0.7) >= 0.7.0
BuildRequires:  crate(rand-0.10) >= 0.10.2
BuildRequires:  crate(rand-core-0.10) >= 0.10.1
BuildRequires:  crate(regex-1) >= 1.13.1
BuildRequires:  crate(regex-automata-0.4) >= 0.4.18
BuildRequires:  crate(regex-syntax-0.8) >= 0.8.11
BuildRequires:  crate(rustc-hash-1) >= 1.1.0
BuildRequires:  crate(rustc-version-0.4) >= 0.4.1
BuildRequires:  crate(rustix-1) >= 1.1.4
BuildRequires:  crate(semver-1) >= 1.0.28
BuildRequires:  crate(serde-1) >= 1.0.229
BuildRequires:  crate(serde-core-1) >= 1.0.229
BuildRequires:  crate(serde-derive-1) >= 1.0.229
BuildRequires:  crate(serde-json-1) >= 1.0.151
BuildRequires:  crate(gdbstub-0.7) >= 0.7.0
BuildRequires:  crate(gdbstub-arch-0.3) >= 0.3.0
BuildRequires:  crate(shlex-1) >= 1.3.0
BuildRequires:  crate(shlex-2) >= 2.0.1
BuildRequires:  crate(slab-0.4) >= 0.4.12
BuildRequires:  crate(strsim-0.11) >= 0.11.1
BuildRequires:  crate(syn-2) >= 2.0.119
BuildRequires:  crate(syn-3) >= 3.0.3
BuildRequires:  crate(tap-1) >= 1.0.1
BuildRequires:  crate(proptest-1/std) >= 1.11.0
BuildRequires:  crate(bit-set-0.8/default) >= 0.8.0
BuildRequires:  crate(bit-vec-0.8/default) >= 0.8.0
BuildRequires:  crate(proptest-macro-0.5) >= 0.5.0
BuildRequires:  crate(regex-syntax-0.8/default) >= 0.8.0
BuildRequires:  crate(rusty-fork-0.3/default) >= 0.3.0
BuildRequires:  crate(tempfile-3/default) >= 3.0.0
BuildRequires:  crate(x86-0.52/default) >= 0.52.0
BuildRequires:  crate(rayon-1/default) >= 1.3.0
BuildRequires:  crate(smol-2) >= 2.0.0
BuildRequires:  crate(tokio-1/rt) >= 1.0.0
BuildRequires:  crate(spin-0.9) >= 0.9.8
BuildRequires:  crate(thiserror-1) >= 1.0.69
BuildRequires:  crate(thiserror-impl-1) >= 1.0.69
BuildRequires:  crate(thiserror-2) >= 2.0.20
BuildRequires:  crate(thiserror-impl-2) >= 2.0.20
BuildRequires:  crate(unicode-ident-1) >= 1.0.24
BuildRequires:  crate(unicode-segmentation-1) >= 1.13.3
BuildRequires:  crate(unicode-xid-0.2) >= 0.2.6
BuildRequires:  crate(untrusted-0.7) >= 0.7.1
BuildRequires:  crate(userfaultfd-0.9) >= 0.9.0
BuildRequires:  crate(userfaultfd-sys-0.6) >= 0.6.0
BuildRequires:  crate(utf8parse-0.2) >= 0.2.2
BuildRequires:  crate(uuid-1) >= 1.24.1
BuildRequires:  crate(vhost-0.17) >= 0.17.0
BuildRequires:  crate(vm-allocator-0.1) >= 0.1.4
BuildRequires:  crate(vm-fdt-0.3) >= 0.3.0
BuildRequires:  crate(vm-memory-0.18) >= 0.18.0
BuildRequires:  crate(vm-superio-0.8) >= 0.8.1
BuildRequires:  crate(vmm-sys-util-0.15) >= 0.15.0
BuildRequires:  crate(walkdir-2/default) >= 2.5.0
BuildRequires:  crate(wyz-0.5) >= 0.5.1
BuildRequires:  crate(zerocopy-0.8) >= 0.8.56
BuildRequires:  crate(zerocopy-derive-0.8) >= 0.8.56
BuildRequires:  crate(zeroize-1) >= 1.9.0
BuildRequires:  crate(zmij-1) >= 1.0.23

%description
Firecracker is a virtual machine monitor that runs microVMs on Linux KVM.

%prep -a
mkdir -p deps/micro-http
tar -xf %{SOURCE1} -C deps/micro-http --strip-components=1
%rust_setup_registry

%build
rm -f Cargo.lock
%buildsystem_rust_build -- --package firecracker

%install
install -D -m 0755 build/cargo_target/release/firecracker %{buildroot}%{_bindir}/firecracker
install -D -m 0644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
install -m 0644 NOTICE THIRD-PARTY %{buildroot}%{_datadir}/licenses/%{name}/

%check
# Run library unit tests. The VMM integration tests require a KVM host, which is unavailable in OBS.
cargo test --offline --package firecracker --lib --jobs 1

%files
%{_bindir}/firecracker
%doc docs/riscv64.md
%{_datadir}/licenses/%{name}/

%changelog
%autochangelog

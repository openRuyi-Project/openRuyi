# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit b3229d591769f23470d1d1d5829dfcf69d7fd46d

Name:           cargo-buckal
Version:        0.1.4
Release:        %autorelease
Summary:        Cargo subcommand for using Buck2 with Rust projects
License:        MIT
URL:            https://github.com/buck2hub/cargo-buckal
VCS:            git:https://github.com/buck2hub/cargo-buckal.git
#!RemoteAsset:  sha256:2c76ed1aaa667afbf5bce052f00233bcda5b25c6d7b32ebe22b8fc1259bb7fa9
Source:         %{url}/archive/%{commit}/cargo-buckal-%{commit}.tar.gz
# Recognize the openRuyi RISC-V Rust target and the packaged Buck2 prelude.
Patch2000:      2000-add-riscv64-toolchain-support.patch
BuildSystem:    rust

BuildOption(prep):   -n %{name}-%{commit}
BuildOption(build):  --bin cargo-buckal

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconf-pkg-config
BuildRequires:  crate(allocative-0.3/default) >= 0.3.6
BuildRequires:  crate(anyhow-1/default) >= 1.0.100
BuildRequires:  crate(bincode-next-3/default) >= 3.1.1
BuildRequires:  crate(bincode-next-3/serde) >= 3.1.1
BuildRequires:  crate(bitflags-2/default) >= 2.10.0
BuildRequires:  crate(blake3-1/default) >= 1.8.2
BuildRequires:  crate(cargo-metadata-0.23/default) >= 0.23.1
BuildRequires:  crate(cargo-platform-0.3/default) >= 0.3.0
BuildRequires:  crate(cargo-util-schemas-0.14/default) >= 0.14.2
BuildRequires:  crate(clap-4/default) >= 4.5.41
BuildRequires:  crate(clap-4/derive) >= 4.5.41
BuildRequires:  crate(colored-3/default) >= 3.1.1
BuildRequires:  crate(daggy-0.9/default) >= 0.9
BuildRequires:  crate(fs-extra-1/default) >= 1.3.0
BuildRequires:  crate(globset-0.4/default) >= 0.4.18
BuildRequires:  crate(hex-0.4/default) >= 0.4.3
BuildRequires:  crate(home-0.5/default) >= 0.5.12
BuildRequires:  crate(include-dir-0.7/default) >= 0.7.4
BuildRequires:  crate(indicatif-0.18/default) >= 0.18.3
BuildRequires:  crate(indoc-2/default) >= 2.0.6
BuildRequires:  crate(inquire-0.9/default) >= 0.9.4
BuildRequires:  crate(itertools-0.15/default) >= 0.15.0
# Cargo resolves the Android branch of rustls-platform-verifier as well.
BuildRequires:  crate(jni-sys-0.4/default) >= 0.4.1
BuildRequires:  crate(log-0.4/default) >= 0.4
BuildRequires:  crate(phf-0.14/default) >= 0.14.0
BuildRequires:  crate(phf-0.14/macros) >= 0.14.0
BuildRequires:  crate(regex-1/default) >= 1.11.2
BuildRequires:  crate(reqwest-0.13/blocking) >= 0.13.4
BuildRequires:  crate(reqwest-0.13/default) >= 0.13.4
BuildRequires:  crate(reqwest-0.13/json) >= 0.13.4
BuildRequires:  crate(reqwest-0.13/query) >= 0.13.4
BuildRequires:  crate(rust-ini-0.21/default) >= 0.21
BuildRequires:  crate(ruzstd-0.9/default) >= 0.9.0
BuildRequires:  crate(semver-1/default) >= 1.0.26
BuildRequires:  crate(serde-1/default) >= 1.0.219
BuildRequires:  crate(serde-derive-1/default) >= 1.0.219
BuildRequires:  crate(serde-json-1/default) >= 1.0.143
BuildRequires:  crate(serde-starlark-0.1/default) >= 0.1.17
BuildRequires:  crate(sha1-0.11/default) >= 0.11.0
BuildRequires:  crate(sha2-0.11/default) >= 0.11.0
BuildRequires:  crate(starlark-syntax-0.14/default) >= 0.14.2
BuildRequires:  crate(tempfile-3/default) >= 3
BuildRequires:  crate(toml-1/default) >= 1.1.5
BuildRequires:  crate(toml-edit-0.25/default) >= 0.25.13
BuildRequires:  crate(url-2/default) >= 2.5.8
BuildRequires:  crate(walkdir-2/default) >= 2.5.0

Requires:       buck2 = 2026.11.15
Requires:       cargo
Requires:       cargo-buckal-bundles = 0.20260803
Requires:       gcc-c++
Requires:       git
Requires:       python3
Requires:       rust

%description
Cargo Buckal generates and runs Buck2 build rules for Cargo projects.
The cargo-buckal-bundles package provides rules for a local buckal cell.

%install
install -Dpm0755 target/release/cargo-buckal %{buildroot}%{_bindir}/cargo-buckal

%check
target/release/cargo-buckal buckal --version | grep -F "buckal %{version}"

%files
%doc README.md
%license LICENSE
%{_bindir}/cargo-buckal

%changelog
%autochangelog

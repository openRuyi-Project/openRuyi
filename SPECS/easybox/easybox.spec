# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit dbcc2aa4164c3e20466c520b7c439562f2ee8e26
%global commands base32,md5sum,sha256sum

Name:           easybox
Version:        0+git20260420.dbcc2aa
Release:        %autorelease
Summary:        Rust multicall toolkit for encoding and checksums
License:        MulanPSL-2.0 AND MIT
URL:            https://gitcode.com/openeuler/easybox
#!RemoteAsset:  sha256:aa12752dcde1928b4e9fc215a734748fd57111e209271da3291c7d4ecfb09572
Source:         https://github.com/openeuler-mirror/easybox/archive/%{commit}/easybox-%{commit}.tar.gz
BuildSystem:    rust

# Limit dependency resolution to the utilities installed by this package.
Patch2000:      2000-limit-workspace-to-packaged-commands.patch

BuildOption(prep):  -n %{name}-%{commit}
BuildOption(build):  --bin easybox --no-default-features --features %{commands}

BuildRequires:  cargo
BuildRequires:  rust >= 1.76
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(clap-3/cargo) >= 3.2.0
BuildRequires:  crate(clap-3/default) >= 3.2.0
BuildRequires:  crate(clap-3/wrap-help) >= 3.2.0
BuildRequires:  crate(clap-complete-3/default) >= 3.1.0
BuildRequires:  crate(data-encoding-2/default) >= 2.1.0
BuildRequires:  crate(data-encoding-macro-0.1/default) >= 0.1.12
BuildRequires:  crate(dunce-1/default) >= 1.0.0
BuildRequires:  crate(errno-0.3/default) >= 0.3.9
BuildRequires:  crate(glob-0.3/default) >= 0.3.0
BuildRequires:  crate(md-5-0.10/default) >= 0.10.6
BuildRequires:  crate(once-cell-1/default) >= 1.13.1
BuildRequires:  crate(os-display-0.1/default) >= 0.1.3
BuildRequires:  crate(phf-0.11/default) >= 0.11.3
BuildRequires:  crate(phf-codegen-0.11/default) >= 0.11.3
BuildRequires:  crate(proc-macro2-1/default) >= 1.0.40
BuildRequires:  crate(quote-1/default) >= 1.0.10
BuildRequires:  crate(regex-1/default) >= 1.10.5
BuildRequires:  crate(textwrap-0.16/default) >= 0.16.1
BuildRequires:  crate(textwrap-0.16/terminal-size) >= 0.16.1
BuildRequires:  crate(thiserror-1/default) >= 1.0.0
BuildRequires:  crate(wild-2/default) >= 2.0.0
BuildRequires:  crate(z85-3/default) = 3.0.5

%description
Easybox provides Rust implementations of common command-line utilities.
This package installs a single easybox binary with Base32 encoding and
decoding and MD5 and SHA-256 checksum utilities.

%install
install -Dpm0755 target/release/easybox %{buildroot}%{_bindir}/easybox
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/MulanPSL-2.0
install -Dpm0644 src/bin/LICENSE %{buildroot}%{_licensedir}/%{name}/multicall-MIT

%check
test "$(printf foo | target/release/easybox base32)" = 'MZXW6==='
test "$(printf 'MZXW6===\n' | target/release/easybox base32 -d)" = 'foo'
test "$(printf foo | target/release/easybox md5sum | cut -d ' ' -f 1)" = 'acbd18db4cc2f85cedef654fccc4a4d8'
test "$(printf foo | target/release/easybox sha256sum | cut -d ' ' -f 1)" = '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae'

%files
%license %{_licensedir}/%{name}/
%doc README.en.md
%{_bindir}/easybox

%changelog
%autochangelog

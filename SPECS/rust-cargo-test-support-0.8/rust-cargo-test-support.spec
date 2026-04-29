# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo-test-support
%global full_version 0.8.1
%global pkgname cargo-test-support-0.8

Name:           rust-cargo-test-support-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "cargo-test-support"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cargo
#!RemoteAsset:  sha256:6ac364115422eabd0cdd5b80523d52747497623636edf7315ea1fe3b3eee7b0c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstream-0.6/default) >= 0.6.21
Requires:       crate(anstyle-1.0/default) >= 1.0.14
Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(cargo-test-macro-0.4/default) >= 0.4.9
Requires:       crate(cargo-util-0.2/default) >= 0.2.27
Requires:       crate(crates-io-0.40/default) >= 0.40.17
Requires:       crate(filetime-0.2/default) >= 0.2.27
Requires:       crate(flate2-1.0/zlib-rs) >= 1.1.9
Requires:       crate(git2-0.20/default) >= 0.20.4
Requires:       crate(glob-0.3/default) >= 0.3.3
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(pasetors-0.7/default) >= 0.7.8
Requires:       crate(pasetors-0.7/paserk) >= 0.7.8
Requires:       crate(pasetors-0.7/serde) >= 0.7.8
Requires:       crate(pasetors-0.7/std) >= 0.7.8
Requires:       crate(pasetors-0.7/v3) >= 0.7.8
Requires:       crate(regex-1.0/default) >= 1.12.3
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(snapbox-0.6/default) >= 0.6.24
Requires:       crate(snapbox-0.6/diff) >= 0.6.24
Requires:       crate(snapbox-0.6/dir) >= 0.6.24
Requires:       crate(snapbox-0.6/json) >= 0.6.24
Requires:       crate(snapbox-0.6/regex) >= 0.6.24
Requires:       crate(snapbox-0.6/term-svg) >= 0.6.24
Requires:       crate(tar-0.4) >= 0.4.45
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47
Requires:       crate(time-0.3/serde) >= 0.3.47
Requires:       crate(toml-0.9/display) >= 0.9.12
Requires:       crate(toml-0.9/serde) >= 0.9.12
Requires:       crate(url-2.0/default) >= 2.5.8
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Requires:       crate(windows-sys-0.60/default) >= 0.60.2
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cargo-test-support"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

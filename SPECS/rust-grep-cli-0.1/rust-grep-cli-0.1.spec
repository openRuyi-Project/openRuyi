# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name grep-cli
%global full_version 0.1.11
%global pkgname grep-cli-0.1

Name:           rust-grep-cli-0.1
Version:        0.1.11
Release:        %autorelease
Summary:        Rust crate "grep-cli"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/ripgrep/tree/master/crates/cli
#!RemoteAsset:  sha256:47f1288f0e06f279f84926fa4c17e3fcd2a22b357927a82f2777f7be26e4cec0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/default) >= 1.6.2
Requires:       crate(bstr-1/std) >= 1.6.2
Requires:       crate(globset-0.4/default) >= 0.4.15
Requires:       crate(libc-0.2/default) >= 0.2.148
Requires:       crate(log-0.4/default) >= 0.4.20
Requires:       crate(termcolor-1/default) >= 1.3.0
Requires:       crate(winapi-util-0.1/default) >= 0.1.6

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "grep-cli"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

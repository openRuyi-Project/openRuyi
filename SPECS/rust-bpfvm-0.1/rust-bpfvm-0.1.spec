# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name      bpfvm
%global full_version    0.1.2
%global pkgname         bpfvm-0.1

Name:           rust-bpfvm-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "bpfvm"
License:        ISC
URL:            https://github.com/tarka/libpledge/bpfvm/
#!RemoteAsset:  sha256:6199736892ea0f6c5746b34ba5e104d61967d55dd61c9a80284133be096d9fbf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/vm) = %{version}

Requires:       crate(libc-0.2/default) >= 0.2.135
Requires:       crate(libc-0.2/extra-traits) >= 0.2.135
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(thiserror-1/default) >= 1.0.37

%description
It is intended for testing cBPF functionality before deployment, e.g. seccomp BPF filters.
Source code for takopackized Rust crate "bpfvm"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

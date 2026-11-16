# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

%global crate_name remoteprocess
%global full_version 0.5.1
%global pkgname remoteprocess-0.5

Name:           rust-remoteprocess-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "remoteprocess"
License:        MIT
URL:            https://github.com/benfred/remoteprocess
#!RemoteAsset:  sha256:8192fa1e574a067848e404651275f19603ac4ec0d8957997597a0495614ddc85
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.1
Requires:       crate(goblin-0.10/default) >= 0.10.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(proc-maps-0.4/default) >= 0.4.0
Requires:       crate(read-process-memory-0.1/default) >= 0.1.6
Requires:       crate(regex-1/default) >= 1.8.3
Requires:       crate(addr2line-0.25/default) >= 0.25.0
Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(memmap2-0.9/default) >= 0.9.7
Requires:       crate(nix-0.26/ptrace) >= 0.26.0
Requires:       crate(nix-0.26/sched) >= 0.26.0
Requires:       crate(nix-0.26/signal) >= 0.26.0
Requires:       crate(object-0.37/default) >= 0.37.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "remoteprocess"

%package     -n %{name}+unwind
Summary:        Cross platform api for getting information on running processes - feature "unwind"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unwind) = %{version}

%description -n %{name}+unwind
This metapackage enables feature "unwind" for the Rust remoteprocess crate.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

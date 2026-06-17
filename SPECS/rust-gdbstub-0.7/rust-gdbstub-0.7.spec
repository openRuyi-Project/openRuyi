# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gdbstub
%global full_version 0.7.10
%global pkgname gdbstub-0.7

Name:           rust-gdbstub-0.7
Version:        0.7.10
Release:        %autorelease
Summary:        Rust crate "gdbstub"
License:        MIT OR Apache-2.0
URL:            https://github.com/daniel5151/gdbstub
#!RemoteAsset:  sha256:5bafc7e33650ab9f05dcc16325f05d56b8d10393114e31a19a353b86fa60cfe7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.3.1
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(managed-0.8) >= 0.8.0
Requires:       crate(num-traits-0.2) >= 0.2.0
Requires:       crate(pastey-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core-error) = %{version}
Provides:       crate(%{pkgname}/dead-code-marker) = %{version}
Provides:       crate(%{pkgname}/paranoid-unsafe) = %{version}

%description
Source code for takopackized Rust crate "gdbstub"

%package     -n %{name}+alloc
Summary:        The GDB Remote Serial Protocol in Rust - feature "alloc" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(managed-0.8/alloc) >= 0.8.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/trace-pkt) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust gdbstub crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std", and "trace-pkt" features.

%package     -n %{name}+default
Summary:        The GDB Remote Serial Protocol in Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/trace-pkt) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gdbstub crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name seccompiler
%global full_version 0.5.0
%global pkgname seccompiler-0.5

Name:           rust-seccompiler-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "seccompiler"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/seccompiler
#!RemoteAsset:  sha256:a4ae55de56877481d112a559bbc12667635fdaf5e005712fd4e2b2fa50ffc884
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.153
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "seccompiler"

%package     -n %{name}+json
Summary:        Provides easy-to-use seccomp-bpf jailing - feature "json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/json) = %{version}

%description -n %{name}+json
This metapackage enables feature "json" for the Rust seccompiler crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Provides easy-to-use seccomp-bpf jailing - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.27
Requires:       crate(serde-1/derive) >= 1.0.27
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust seccompiler crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Provides easy-to-use seccomp-bpf jailing - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.9
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust seccompiler crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

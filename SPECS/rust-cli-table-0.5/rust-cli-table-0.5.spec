# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cli-table
%global full_version 0.5.0
%global pkgname cli-table-0.5

Name:           rust-cli-table-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "cli-table"
License:        MIT OR Apache-2.0
URL:            https://github.com/devashishdxt/cli-table
#!RemoteAsset:  sha256:14da8d951cef7cc4f13ccc9b744d736963d57863c7e6fc33c070ea274546082c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(termcolor-1/default) >= 1.4.1
Requires:       crate(unicode-width-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/doc) = %{version}
Provides:       crate(%{pkgname}/title) = %{version}

%description
Source code for takopackized Rust crate "cli-table"

%package     -n %{name}+cli-table-derive
Summary:        Printing tables on command line - feature "cli-table-derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cli-table-derive-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/cli-table-derive) = %{version}

%description -n %{name}+cli-table-derive
This metapackage enables feature "cli-table-derive" for the Rust cli-table crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+csv
Summary:        Printing tables on command line - feature "csv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(csv-1/default) >= 1.3.1
Provides:       crate(%{pkgname}/csv) = %{version}

%description -n %{name}+csv
This metapackage enables feature "csv" for the Rust cli-table crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Printing tables on command line - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/csv) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust cli-table crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Printing tables on command line - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cli-table-derive) = %{version}
Requires:       crate(%{pkgname}/title) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust cli-table crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

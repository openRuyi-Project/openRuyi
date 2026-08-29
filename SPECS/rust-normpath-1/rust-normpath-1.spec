# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name normpath
%global full_version 1.5.0
%global pkgname normpath-1

Name:           rust-normpath-1
Version:        1.5.0
Release:        %autorelease
Summary:        Rust crate "normpath"
License:        MIT OR Apache-2.0
URL:            https://github.com/dylni/normpath
#!RemoteAsset:  sha256:bf23ab2b905654b4cb177e30b629937b3868311d4e1cba859f899c041046e69b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "normpath"

%package     -n %{name}+localization
Summary:        More reliable path manipulation - feature "localization"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-ui-shell) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-ui-windowsandmessaging) >= 0.61.0
Provides:       crate(%{pkgname}/localization) = %{version}

%description -n %{name}+localization
This metapackage enables feature "localization" for the Rust normpath crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+print-bytes
Summary:        More reliable path manipulation - feature "print_bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(print-bytes-2/default) >= 2.0.0
Requires:       crate(print-bytes-2/os-str-bytes) >= 2.0.0
Provides:       crate(%{pkgname}/print-bytes) = %{version}

%description -n %{name}+print-bytes
This metapackage enables feature "print_bytes" for the Rust normpath crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        More reliable path manipulation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust normpath crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uniquote
Summary:        More reliable path manipulation - feature "uniquote"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uniquote-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/uniquote) = %{version}

%description -n %{name}+uniquote
This metapackage enables feature "uniquote" for the Rust normpath crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

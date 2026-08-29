# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name python-pkginfo
%global full_version 0.6.8
%global pkgname python-pkginfo-0.6

Name:           rust-python-pkginfo-0.6
Version:        0.6.8
Release:        %autorelease
Summary:        Rust crate "python-pkginfo"
License:        MIT
URL:            https://github.com/PyO3/python-pkginfo-rs
#!RemoteAsset:  sha256:229fe47647d6602b9b0934b21fab8aece1c5a5aeb0a934196a14355fec656623
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:         0001-fix-dependency-ranges.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(flate2-1/default) >= 1.0.33
Requires:       crate(fs-err-3/default) >= 3.0.0
Requires:       crate(mailparse-0.16/default) >= 0.16.0
Requires:       crate(rfc2047-decoder-1/default) >= 1.0.6
Requires:       crate(tar-0.4/default) >= 0.4.41
Requires:       crate(thiserror-2/default) >= 2.0.3
Requires:       crate(zip-8/deflate) >= 8.6.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "python-pkginfo"

%package     -n %{name}+bzip2
Summary:        Parse Python package metadata from sdist and bdists and etc - feature "bzip2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bzip2-0.5/default) >= 0.5.2
Provides:       crate(%{pkgname}/bzip2) = %{version}

%description -n %{name}+bzip2
This metapackage enables feature "bzip2" for the Rust python-pkginfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deprecated-formats
Summary:        Parse Python package metadata from sdist and bdists and etc - feature "deprecated-formats"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bzip2) = %{version}
Requires:       crate(%{pkgname}/xz) = %{version}
Requires:       crate(zip-8/bzip2) >= 8.6.0
Requires:       crate(zip-8/deflate) >= 8.6.0
Provides:       crate(%{pkgname}/deprecated-formats) = %{version}

%description -n %{name}+deprecated-formats
This metapackage enables feature "deprecated-formats" for the Rust python-pkginfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Parse Python package metadata from sdist and bdists and etc - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.210
Requires:       crate(serde-1/derive) >= 1.0.210
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust python-pkginfo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xz
Summary:        Parse Python package metadata from sdist and bdists and etc - feature "xz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(xz2-0.1/default) >= 0.1.7
Provides:       crate(%{pkgname}/xz) = %{version}

%description -n %{name}+xz
This metapackage enables feature "xz" for the Rust python-pkginfo crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

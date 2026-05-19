# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libcst
%global full_version 1.8.6
%global pkgname libcst-1.0

Name:           rust-libcst-1.0
Version:        1.8.6
Release:        %autorelease
Summary:        Rust crate "libcst"
License:        MIT AND (MIT AND PSF-2.0)
URL:            https://github.com/Instagram/LibCST
#!RemoteAsset:  sha256:6aea7143e4a0ed59b87a1ee71e198500889f8b005311136be15e84c97a6fcd8d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(annotate-snippets-0.11/default) >= 0.11.5
Requires:       crate(libcst-derive-1.0/default) >= 1.8.6
Requires:       crate(memchr-2.0/default) >= 2.8.0
Requires:       crate(paste-1.0/default) >= 1.0.15
Requires:       crate(peg-0.8/default) >= 0.8.5
Requires:       crate(regex-1.0/default) >= 1.12.3
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "libcst"

%package     -n %{name}+py
Summary:        Python parser and Concrete Syntax Tree library - feature "py" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pyo3)
Requires:       crate(pyo3-0.26/extension-module) >= 0.26.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/py)

%description -n %{name}+py
This metapackage enables feature "py" for the Rust libcst crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+pyo3
Summary:        Python parser and Concrete Syntax Tree library - feature "pyo3"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-0.26/default) >= 0.26.0
Provides:       crate(%{pkgname}/pyo3)

%description -n %{name}+pyo3
This metapackage enables feature "pyo3" for the Rust libcst crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+trace
Summary:        Python parser and Concrete Syntax Tree library - feature "trace"
Requires:       crate(%{pkgname})
Requires:       crate(peg-0.8/trace) >= 0.8.5
Provides:       crate(%{pkgname}/trace)

%description -n %{name}+trace
This metapackage enables feature "trace" for the Rust libcst crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

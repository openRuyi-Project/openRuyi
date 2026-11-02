# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pulldown-cmark
%global full_version 0.13.3
%global pkgname pulldown-cmark-0.13

Name:           rust-pulldown-cmark-0.13
Version:        0.13.3
Release:        %autorelease
Summary:        Rust crate "pulldown-cmark"
License:        MIT
URL:            https://github.com/raphlinus/pulldown-cmark
#!RemoteAsset:  sha256:7c3a14896dfa883796f1cb410461aef38810ea05f2b2c33c5aded3649095fdad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(memchr-2/default) >= 2.5.0
Requires:       crate(unicase-2/default) >= 2.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/gen-tests) = %{version}

%description
Source code for takopackized Rust crate "pulldown-cmark"

%package     -n %{name}+default
Summary:        Pull parser for CommonMark - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/getopts) = %{version}
Requires:       crate(%{pkgname}/html) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust pulldown-cmark crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getopts
Summary:        Pull parser for CommonMark - feature "getopts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getopts-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/getopts) = %{version}

%description -n %{name}+getopts
This metapackage enables feature "getopts" for the Rust pulldown-cmark crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pulldown-cmark-escape
Summary:        Pull parser for CommonMark - feature "pulldown-cmark-escape" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pulldown-cmark-escape-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/html) = %{version}
Provides:       crate(%{pkgname}/pulldown-cmark-escape) = %{version}

%description -n %{name}+pulldown-cmark-escape
This metapackage enables feature "pulldown-cmark-escape" for the Rust pulldown-cmark crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "html" feature.

%package     -n %{name}+serde
Summary:        Pull parser for CommonMark - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pulldown-cmark crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simd
Summary:        Pull parser for CommonMark - feature "simd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pulldown-cmark-escape-0.11/simd) >= 0.11.0
Provides:       crate(%{pkgname}/simd) = %{version}

%description -n %{name}+simd
This metapackage enables feature "simd" for the Rust pulldown-cmark crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

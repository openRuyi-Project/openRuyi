# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name im-rc
%global full_version 15.1.0
%global pkgname im-rc-15.0

Name:           rust-im-rc-15.0
Version:        15.1.0
Release:        %autorelease
Summary:        Rust crate "im-rc"
License:        MPL-2.0+
URL:            http://immutable.rs/
#!RemoteAsset:  sha256:af1955a75fa080c677d3972822ec4bad316169ab1cfc6c257a942c2265dbe5fe
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitmaps-2.0/default) >= 2.1.0
Requires:       crate(rand-core-0.6/default) >= 0.6.4
Requires:       crate(rand-xoshiro-0.6/default) >= 0.6.0
Requires:       crate(sized-chunks-0.6/default) >= 0.6.5
Requires:       crate(typenum-1.0/default) >= 1.19.0
Requires:       crate(version-check-0.9/default) >= 0.9.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/debug)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "im-rc"

%package     -n %{name}+arbitrary
Summary:        Immutable collection datatypes (the fast but not thread safe version) - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/default) >= 1.1
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust im-rc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pool
Summary:        Immutable collection datatypes (the fast but not thread safe version) - feature "pool"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/refpool)
Requires:       crate(sized-chunks-0.6/refpool) >= 0.6.5
Provides:       crate(%{pkgname}/pool)

%description -n %{name}+pool
This metapackage enables feature "pool" for the Rust im-rc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest
Summary:        Immutable collection datatypes (the fast but not thread safe version) - feature "proptest"
Requires:       crate(%{pkgname})
Requires:       crate(proptest-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/proptest)

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust im-rc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Immutable collection datatypes (the fast but not thread safe version) - feature "quickcheck"
Requires:       crate(%{pkgname})
Requires:       crate(quickcheck-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/quickcheck)

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust im-rc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Immutable collection datatypes (the fast but not thread safe version) - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust im-rc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+refpool
Summary:        Immutable collection datatypes (the fast but not thread safe version) - feature "refpool"
Requires:       crate(%{pkgname})
Requires:       crate(refpool-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/refpool)

%description -n %{name}+refpool
This metapackage enables feature "refpool" for the Rust im-rc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Immutable collection datatypes (the fast but not thread safe version) - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust im-rc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

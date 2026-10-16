# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tera
%global full_version 1.20.1
%global pkgname tera-1

Name:           rust-tera-1
Version:        1.20.1
Release:        %autorelease
Summary:        Rust crate "tera"
License:        MIT
URL:            https://keats.github.io/tera/
#!RemoteAsset:  sha256:e8004bca281f2d32df3bacd59bc67b312cb4c70cea46cbd79dbe8ac5ed206722
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(globwalk-0.9/default) >= 0.9.1
Requires:       crate(lazy-static-1/default) >= 1.4.0
Requires:       crate(pest-2/default) >= 2.5.5
Requires:       crate(pest-derive-2/default) >= 2.5.5
Requires:       crate(regex-1/default) >= 1.7.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(unicode-segmentation-1/default) >= 1.12.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tera"

%package     -n %{name}+builtins
Summary:        Template engine based on Jinja2/Django templates - feature "builtins" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/chrono-tz) = %{version}
Requires:       crate(%{pkgname}/humansize) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/slug) = %{version}
Requires:       crate(%{pkgname}/urlencode) = %{version}
Provides:       crate(%{pkgname}/builtins) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+builtins
This metapackage enables feature "builtins" for the Rust tera crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+chrono
Summary:        Template engine based on Jinja2/Django templates - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.27
Requires:       crate(chrono-0.4/std) >= 0.4.27
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust tera crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono-tz
Summary:        Template engine based on Jinja2/Django templates - feature "chrono-tz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-tz-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/chrono-tz) = %{version}

%description -n %{name}+chrono-tz
This metapackage enables feature "chrono-tz" for the Rust tera crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+date-locale
Summary:        Template engine based on Jinja2/Django templates - feature "date-locale"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/builtins) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.27
Requires:       crate(chrono-0.4/std) >= 0.4.27
Requires:       crate(chrono-0.4/unstable-locales) >= 0.4.27
Provides:       crate(%{pkgname}/date-locale) = %{version}

%description -n %{name}+date-locale
This metapackage enables feature "date-locale" for the Rust tera crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+humansize
Summary:        Template engine based on Jinja2/Django templates - feature "humansize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(humansize-2/default) >= 2.1.0
Provides:       crate(%{pkgname}/humansize) = %{version}

%description -n %{name}+humansize
This metapackage enables feature "humansize" for the Rust tera crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+percent-encoding
Summary:        Template engine based on Jinja2/Django templates - feature "percent-encoding" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(percent-encoding-2/default) >= 2.2.0
Provides:       crate(%{pkgname}/percent-encoding) = %{version}
Provides:       crate(%{pkgname}/urlencode) = %{version}

%description -n %{name}+percent-encoding
This metapackage enables feature "percent-encoding" for the Rust tera crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "urlencode" feature.

%package     -n %{name}+preserve-order
Summary:        Template engine based on Jinja2/Django templates - feature "preserve_order"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/preserve-order) >= 1.0.0
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+preserve-order
This metapackage enables feature "preserve_order" for the Rust tera crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Template engine based on Jinja2/Django templates - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust tera crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+slug
Summary:        Template engine based on Jinja2/Django templates - feature "slug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(slug-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/slug) = %{version}

%description -n %{name}+slug
This metapackage enables feature "slug" for the Rust tera crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

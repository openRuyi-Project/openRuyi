# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name handlebars
%global full_version 6.4.4
%global pkgname handlebars-6

Name:           rust-handlebars-6
Version:        6.4.4
Release:        %autorelease
Summary:        Rust crate "handlebars"
License:        MIT
URL:            https://github.com/sunng87/handlebars-rust
#!RemoteAsset:  sha256:75c54236f9045c8004a77942bebc52145b4844639db934a5c70fe08617fbe61a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(num-order-1/default) >= 1.2.0
Requires:       crate(pest-2/default) >= 2.2.0
Requires:       crate(pest-derive-2/default) >= 2.2.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.39
Requires:       crate(thiserror-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-logging) = %{version}

%description
Source code for takopackized Rust crate "handlebars"

%package     -n %{name}+heck
Summary:        Handlebars templating implemented in Rust - feature "heck" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(heck-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/heck) = %{version}
Provides:       crate(%{pkgname}/string-helpers) = %{version}

%description -n %{name}+heck
This metapackage enables feature "heck" for the Rust handlebars crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "string_helpers" feature.

%package     -n %{name}+preserve-json-order
Summary:        Handlebars templating implemented in Rust - feature "preserve_json_order" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/preserve-order) >= 1.0.39
Provides:       crate(%{pkgname}/preserve-json-order) = %{version}
Provides:       crate(%{pkgname}/testing) = %{version}

%description -n %{name}+preserve-json-order
This metapackage enables feature "preserve_json_order" for the Rust handlebars crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "testing" feature.

%package     -n %{name}+rhai
Summary:        Handlebars templating implemented in Rust - feature "rhai" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rhai-1/default) >= 1.16.1
Requires:       crate(rhai-1/serde) >= 1.16.1
Requires:       crate(rhai-1/sync) >= 1.16.1
Provides:       crate(%{pkgname}/rhai) = %{version}
Provides:       crate(%{pkgname}/script-helper) = %{version}

%description -n %{name}+rhai
This metapackage enables feature "rhai" for the Rust handlebars crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "script_helper" feature.

%package     -n %{name}+rust-embed
Summary:        Handlebars templating implemented in Rust - feature "rust-embed"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-embed-8/default) >= 8.0.0
Requires:       crate(rust-embed-8/include-exclude) >= 8.0.0
Provides:       crate(%{pkgname}/rust-embed) = %{version}

%description -n %{name}+rust-embed
This metapackage enables feature "rust-embed" for the Rust handlebars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+walkdir
Summary:        Handlebars templating implemented in Rust - feature "walkdir" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(walkdir-2/default) >= 2.2.3
Provides:       crate(%{pkgname}/dir-source) = %{version}
Provides:       crate(%{pkgname}/walkdir) = %{version}

%description -n %{name}+walkdir
This metapackage enables feature "walkdir" for the Rust handlebars crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dir_source" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

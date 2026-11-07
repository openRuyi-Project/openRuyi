# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stdweb
%global full_version 0.4.20
%global pkgname stdweb-0.4

Name:           rust-stdweb-0.4
Version:        0.4.20
Release:        %autorelease
Summary:        Rust crate "stdweb"
License:        MIT OR Apache-2.0
URL:            https://github.com/koute/stdweb
#!RemoteAsset:  sha256:d022496b16281348b52d0e30ae99e01a73d737b2f45d38fed4edf79f9325a1d5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(discard-1/default) >= 1.0.3
Requires:       crate(rustc-version-0.2) >= 0.2.0
Requires:       crate(stdweb-derive-0.5/default) >= 0.5.3
Requires:       crate(stdweb-internal-macros-0.2/default) >= 0.2.9
Requires:       crate(stdweb-internal-runtime-0.1/default) >= 0.1.0
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/docs-rs) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/web-test) = %{version}

%description
Source code for takopackized Rust crate "stdweb"

%package     -n %{name}+default
Summary:        Standard library for the client-side Web - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-channel-preview
Summary:        Standard library for the client-side Web - feature "futures-channel-preview"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-channel-preview-0.3.0-alpha.15/default) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/futures-channel-preview) = %{version}

%description -n %{name}+futures-channel-preview
This metapackage enables feature "futures-channel-preview" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core-preview
Summary:        Standard library for the client-side Web - feature "futures-core-preview"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-preview-0.3.0-alpha.15/default) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/futures-core-preview) = %{version}

%description -n %{name}+futures-core-preview
This metapackage enables feature "futures-core-preview" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-executor-preview
Summary:        Standard library for the client-side Web - feature "futures-executor-preview"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-executor-preview-0.3.0-alpha.15/default) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/futures-executor-preview) = %{version}

%description -n %{name}+futures-executor-preview
This metapackage enables feature "futures-executor-preview" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-support
Summary:        Standard library for the client-side Web - feature "futures-support" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-channel-preview) = %{version}
Requires:       crate(%{pkgname}/futures-core-preview) = %{version}
Requires:       crate(%{pkgname}/futures-executor-preview) = %{version}
Requires:       crate(%{pkgname}/futures-util-preview) = %{version}
Provides:       crate(%{pkgname}/experimental-features-which-may-break-on-minor-version-bumps) = %{version}
Provides:       crate(%{pkgname}/futures-support) = %{version}

%description -n %{name}+futures-support
This metapackage enables feature "futures-support" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "experimental_features_which_may_break_on_minor_version_bumps" feature.

%package     -n %{name}+futures-util-preview
Summary:        Standard library for the client-side Web - feature "futures-util-preview"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-preview-0.3.0-alpha.15/default) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/futures-util-preview) = %{version}

%description -n %{name}+futures-util-preview
This metapackage enables feature "futures-util-preview" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Standard library for the client-side Web - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Standard library for the client-side Web - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust stdweb crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

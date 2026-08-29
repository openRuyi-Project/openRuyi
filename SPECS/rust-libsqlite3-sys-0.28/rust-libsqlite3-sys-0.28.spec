# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libsqlite3-sys
%global full_version 0.28.0
%global pkgname libsqlite3-sys-0.28

Name:           rust-libsqlite3-sys-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "libsqlite3-sys"
License:        MIT
URL:            https://github.com/rusqlite/rusqlite
#!RemoteAsset:  sha256:0c10584274047cb335c23d3e61bcef8e323adae7c5c8c760540f73610177fc3f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bundled-bindings) = %{version}
Provides:       crate(%{pkgname}/in-gecko) = %{version}
Provides:       crate(%{pkgname}/sqlcipher) = %{version}
Provides:       crate(%{pkgname}/unlock-notify) = %{version}
Provides:       crate(%{pkgname}/wasm32-wasi-vfs) = %{version}
Provides:       crate(%{pkgname}/with-asan) = %{version}

%description
Source code for takopackized Rust crate "libsqlite3-sys"

%package     -n %{name}+bindgen
Summary:        Native bindings to the libsqlite3 library - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.69/runtime) >= 0.69.0
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+buildtime-bindgen
Summary:        Native bindings to the libsqlite3 library - feature "buildtime_bindgen" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bindgen) = %{version}
Requires:       crate(%{pkgname}/pkg-config) = %{version}
Requires:       crate(%{pkgname}/vcpkg) = %{version}
Provides:       crate(%{pkgname}/buildtime-bindgen) = %{version}
Provides:       crate(%{pkgname}/preupdate-hook) = %{version}

%description -n %{name}+buildtime-bindgen
This metapackage enables feature "buildtime_bindgen" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "preupdate_hook" feature.

%package     -n %{name}+bundled
Summary:        Native bindings to the libsqlite3 library - feature "bundled" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bundled-bindings) = %{version}
Requires:       crate(%{pkgname}/cc) = %{version}
Provides:       crate(%{pkgname}/bundled) = %{version}
Provides:       crate(%{pkgname}/bundled-sqlcipher) = %{version}
Provides:       crate(%{pkgname}/bundled-windows) = %{version}

%description -n %{name}+bundled
This metapackage enables feature "bundled" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bundled-sqlcipher", and "bundled-windows" features.

%package     -n %{name}+bundled-sqlcipher-vendored-openssl
Summary:        Native bindings to the libsqlite3 library - feature "bundled-sqlcipher-vendored-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bundled-sqlcipher) = %{version}
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.0
Provides:       crate(%{pkgname}/bundled-sqlcipher-vendored-openssl) = %{version}

%description -n %{name}+bundled-sqlcipher-vendored-openssl
This metapackage enables feature "bundled-sqlcipher-vendored-openssl" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cc
Summary:        Native bindings to the libsqlite3 library - feature "cc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/cc) = %{version}

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loadable-extension
Summary:        Native bindings to the libsqlite3 library - feature "loadable_extension"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/prettyplease) = %{version}
Requires:       crate(%{pkgname}/quote) = %{version}
Requires:       crate(%{pkgname}/syn) = %{version}
Provides:       crate(%{pkgname}/loadable-extension) = %{version}

%description -n %{name}+loadable-extension
This metapackage enables feature "loadable_extension" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+min-sqlite-version-3-14-0
Summary:        Native bindings to the libsqlite3 library - feature "min_sqlite_version_3_14_0" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pkg-config) = %{version}
Requires:       crate(%{pkgname}/vcpkg) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/min-sqlite-version-3-14-0) = %{version}

%description -n %{name}+min-sqlite-version-3-14-0
This metapackage enables feature "min_sqlite_version_3_14_0" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+openssl-sys
Summary:        Native bindings to the libsqlite3 library - feature "openssl-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(openssl-sys-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/openssl-sys) = %{version}

%description -n %{name}+openssl-sys
This metapackage enables feature "openssl-sys" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkg-config
Summary:        Native bindings to the libsqlite3 library - feature "pkg-config"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pkg-config-0.3/default) >= 0.3.19
Provides:       crate(%{pkgname}/pkg-config) = %{version}

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prettyplease
Summary:        Native bindings to the libsqlite3 library - feature "prettyplease"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prettyplease-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/prettyplease) = %{version}

%description -n %{name}+prettyplease
This metapackage enables feature "prettyplease" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quote
Summary:        Native bindings to the libsqlite3 library - feature "quote"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quote-1) >= 1.0.0
Provides:       crate(%{pkgname}/quote) = %{version}

%description -n %{name}+quote
This metapackage enables feature "quote" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+session
Summary:        Native bindings to the libsqlite3 library - feature "session"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/buildtime-bindgen) = %{version}
Requires:       crate(%{pkgname}/preupdate-hook) = %{version}
Provides:       crate(%{pkgname}/session) = %{version}

%description -n %{name}+session
This metapackage enables feature "session" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syn
Summary:        Native bindings to the libsqlite3 library - feature "syn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/visit-mut) >= 2.0.0
Provides:       crate(%{pkgname}/syn) = %{version}

%description -n %{name}+syn
This metapackage enables feature "syn" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vcpkg
Summary:        Native bindings to the libsqlite3 library - feature "vcpkg"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vcpkg-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/vcpkg) = %{version}

%description -n %{name}+vcpkg
This metapackage enables feature "vcpkg" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libsqlite3-sys
%global full_version 0.34.0
%global pkgname libsqlite3-sys-0.34

Name:           rust-libsqlite3-sys-0.34
Version:        0.34.0
Release:        %autorelease
Summary:        Rust crate "libsqlite3-sys"
License:        MIT
URL:            https://github.com/rusqlite/rusqlite
#!RemoteAsset:  sha256:91632f3b4fb6bd1d72aa3d78f41ffecfcf2b1a6648d8c241dbe7dbfaf4875e15
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/bundled-bindings)
Provides:       crate(%{pkgname}/column-metadata)
Provides:       crate(%{pkgname}/in-gecko)
Provides:       crate(%{pkgname}/sqlcipher)
Provides:       crate(%{pkgname}/unlock-notify)
Provides:       crate(%{pkgname}/wasm32-wasi-vfs)
Provides:       crate(%{pkgname}/with-asan)

%description
Source code for takopackized Rust crate "libsqlite3-sys"

%package     -n %{name}+bindgen
Summary:        Native bindings to the libsqlite3 library - feature "bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(bindgen-0.71/prettyplease) >= 0.71.0
Requires:       crate(bindgen-0.71/runtime) >= 0.71.0
Provides:       crate(%{pkgname}/bindgen)

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+buildtime-bindgen
Summary:        Native bindings to the libsqlite3 library - feature "buildtime_bindgen" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bindgen)
Requires:       crate(%{pkgname}/pkg-config)
Requires:       crate(%{pkgname}/vcpkg)
Provides:       crate(%{pkgname}/buildtime-bindgen)
Provides:       crate(%{pkgname}/preupdate-hook)

%description -n %{name}+buildtime-bindgen
This metapackage enables feature "buildtime_bindgen" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "preupdate_hook" feature.

%package     -n %{name}+bundled
Summary:        Native bindings to the libsqlite3 library - feature "bundled" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bundled-bindings)
Requires:       crate(%{pkgname}/cc)
Provides:       crate(%{pkgname}/bundled)
Provides:       crate(%{pkgname}/bundled-sqlcipher)
Provides:       crate(%{pkgname}/bundled-windows)

%description -n %{name}+bundled
This metapackage enables feature "bundled" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bundled-sqlcipher", and "bundled-windows" features.

%package     -n %{name}+bundled-sqlcipher-vendored-openssl
Summary:        Native bindings to the libsqlite3 library - feature "bundled-sqlcipher-vendored-openssl"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bundled-sqlcipher)
Requires:       crate(openssl-sys-0.9/vendored) >= 0.9.103
Provides:       crate(%{pkgname}/bundled-sqlcipher-vendored-openssl)

%description -n %{name}+bundled-sqlcipher-vendored-openssl
This metapackage enables feature "bundled-sqlcipher-vendored-openssl" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cc
Summary:        Native bindings to the libsqlite3 library - feature "cc"
Requires:       crate(%{pkgname})
Requires:       crate(cc-1.0/default) >= 1.2.58
Provides:       crate(%{pkgname}/cc)

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loadable-extension
Summary:        Native bindings to the libsqlite3 library - feature "loadable_extension"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/prettyplease)
Requires:       crate(%{pkgname}/quote)
Requires:       crate(%{pkgname}/syn)
Provides:       crate(%{pkgname}/loadable-extension)

%description -n %{name}+loadable-extension
This metapackage enables feature "loadable_extension" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+min-sqlite-version-3-14-0
Summary:        Native bindings to the libsqlite3 library - feature "min_sqlite_version_3_14_0" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pkg-config)
Requires:       crate(%{pkgname}/vcpkg)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/min-sqlite-version-3-14-0)

%description -n %{name}+min-sqlite-version-3-14-0
This metapackage enables feature "min_sqlite_version_3_14_0" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+openssl-sys
Summary:        Native bindings to the libsqlite3 library - feature "openssl-sys"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-sys-0.9/default) >= 0.9.103
Provides:       crate(%{pkgname}/openssl-sys)

%description -n %{name}+openssl-sys
This metapackage enables feature "openssl-sys" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkg-config
Summary:        Native bindings to the libsqlite3 library - feature "pkg-config"
Requires:       crate(%{pkgname})
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Provides:       crate(%{pkgname}/pkg-config)

%description -n %{name}+pkg-config
This metapackage enables feature "pkg-config" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prettyplease
Summary:        Native bindings to the libsqlite3 library - feature "prettyplease"
Requires:       crate(%{pkgname})
Requires:       crate(prettyplease-0.2/default) >= 0.2.20
Provides:       crate(%{pkgname}/prettyplease)

%description -n %{name}+prettyplease
This metapackage enables feature "prettyplease" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quote
Summary:        Native bindings to the libsqlite3 library - feature "quote"
Requires:       crate(%{pkgname})
Requires:       crate(quote-1.0) >= 1.0.36
Provides:       crate(%{pkgname}/quote)

%description -n %{name}+quote
This metapackage enables feature "quote" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+session
Summary:        Native bindings to the libsqlite3 library - feature "session"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/buildtime-bindgen)
Requires:       crate(%{pkgname}/preupdate-hook)
Provides:       crate(%{pkgname}/session)

%description -n %{name}+session
This metapackage enables feature "session" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syn
Summary:        Native bindings to the libsqlite3 library - feature "syn"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/default) >= 2.0.72
Requires:       crate(syn-2.0/extra-traits) >= 2.0.72
Requires:       crate(syn-2.0/full) >= 2.0.72
Requires:       crate(syn-2.0/visit-mut) >= 2.0.72
Provides:       crate(%{pkgname}/syn)

%description -n %{name}+syn
This metapackage enables feature "syn" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vcpkg
Summary:        Native bindings to the libsqlite3 library - feature "vcpkg"
Requires:       crate(%{pkgname})
Requires:       crate(vcpkg-0.2/default) >= 0.2.15
Provides:       crate(%{pkgname}/vcpkg)

%description -n %{name}+vcpkg
This metapackage enables feature "vcpkg" for the Rust libsqlite3-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

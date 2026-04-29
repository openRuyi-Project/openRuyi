# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-features
%global full_version 0.43.1
%global pkgname gix-features-0.43

Name:           rust-gix-features-0.43
Version:        0.43.1
Release:        %autorelease
Summary:        Rust crate "gix-features"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:cd1543cd9b8abcbcebaa1a666a5c168ee2cda4dea50d3961ee0e6d1c42f81e5b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(libc-0.2/default) >= 0.2.184
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cache-efficiency-debug)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-features"

%package     -n %{name}+crc32
Summary:        Integrate various capabilities using compile-time feature flags - feature "crc32"
Requires:       crate(%{pkgname})
Requires:       crate(crc32fast-1.0/default) >= 1.5.0
Provides:       crate(%{pkgname}/crc32)

%description -n %{name}+crc32
This metapackage enables feature "crc32" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Integrate various capabilities using compile-time feature flags - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fs-read-dir
Summary:        Integrate various capabilities using compile-time feature flags - feature "fs-read-dir"
Requires:       crate(%{pkgname})
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/fs-read-dir)

%description -n %{name}+fs-read-dir
This metapackage enables feature "fs-read-dir" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-pipe
Summary:        Integrate various capabilities using compile-time feature flags - feature "io-pipe"
Requires:       crate(%{pkgname})
Requires:       crate(bytes-1.0/default) >= 1.11.1
Provides:       crate(%{pkgname}/io-pipe)

%description -n %{name}+io-pipe
This metapackage enables feature "io-pipe" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Integrate various capabilities using compile-time feature flags - feature "once_cell"
Requires:       crate(%{pkgname})
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Provides:       crate(%{pkgname}/once-cell)

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Integrate various capabilities using compile-time feature flags - feature "parallel"
Requires:       crate(%{pkgname})
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.15
Requires:       crate(parking-lot-0.12) >= 0.12.5
Provides:       crate(%{pkgname}/parallel)

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prodash
Summary:        Integrate various capabilities using compile-time feature flags - feature "prodash" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(prodash-30.0/default) >= 30.0.1
Provides:       crate(%{pkgname}/prodash)
Provides:       crate(%{pkgname}/progress)

%description -n %{name}+prodash
This metapackage enables feature "prodash" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "progress" feature.

%package     -n %{name}+progress-unit-bytes
Summary:        Integrate various capabilities using compile-time feature flags - feature "progress-unit-bytes"
Requires:       crate(%{pkgname})
Requires:       crate(bytesize-2.0/default) >= 2.0.1
Requires:       crate(prodash-30.0/unit-bytes) >= 30.0.1
Provides:       crate(%{pkgname}/progress-unit-bytes)

%description -n %{name}+progress-unit-bytes
This metapackage enables feature "progress-unit-bytes" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+progress-unit-human-numbers
Summary:        Integrate various capabilities using compile-time feature flags - feature "progress-unit-human-numbers"
Requires:       crate(%{pkgname})
Requires:       crate(prodash-30.0/unit-human) >= 30.0.1
Provides:       crate(%{pkgname}/progress-unit-human-numbers)

%description -n %{name}+progress-unit-human-numbers
This metapackage enables feature "progress-unit-human-numbers" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Integrate various capabilities using compile-time feature flags - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(gix-trace-0.1/tracing) >= 0.1.18
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-detail
Summary:        Integrate various capabilities using compile-time feature flags - feature "tracing-detail"
Requires:       crate(%{pkgname})
Requires:       crate(gix-trace-0.1/tracing-detail) >= 0.1.18
Provides:       crate(%{pkgname}/tracing-detail)

%description -n %{name}+tracing-detail
This metapackage enables feature "tracing-detail" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+walkdir
Summary:        Integrate various capabilities using compile-time feature flags - feature "walkdir"
Requires:       crate(%{pkgname})
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Provides:       crate(%{pkgname}/walkdir)

%description -n %{name}+walkdir
This metapackage enables feature "walkdir" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib
Summary:        Integrate various capabilities using compile-time feature flags - feature "zlib" and 5 more
Requires:       crate(%{pkgname})
Requires:       crate(flate2-1.0/zlib-rs) >= 1.1.9
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname}/zlib)
Provides:       crate(%{pkgname}/zlib-ng)
Provides:       crate(%{pkgname}/zlib-ng-compat)
Provides:       crate(%{pkgname}/zlib-rs)
Provides:       crate(%{pkgname}/zlib-rust-backend)
Provides:       crate(%{pkgname}/zlib-stock)

%description -n %{name}+zlib
This metapackage enables feature "zlib" for the Rust gix-features crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "zlib-ng", "zlib-ng-compat", "zlib-rs", "zlib-rust-backend", and "zlib-stock" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

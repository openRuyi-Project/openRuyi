# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lopdf
%global full_version 0.38.0
%global pkgname lopdf-0.38

Name:           rust-lopdf-0.38
Version:        0.38.0
Release:        %autorelease
Summary:        Rust crate "lopdf"
License:        MIT
URL:            https://github.com/J-F-Liu/lopdf
#!RemoteAsset:  sha256:c7184fdea2bc3cd272a1acec4030c321a8f9875e877b3f92a53f2f6033fdc289
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aes-0.8/default) >= 0.8.4
Requires:       crate(bitflags-2/default) >= 2.8.0
Requires:       crate(cbc-0.1/default) >= 0.1.2
Requires:       crate(ecb-0.1/default) >= 0.1.2
Requires:       crate(encoding-rs-0.8/default) >= 0.8.32
Requires:       crate(flate2-1/default) >= 1.0.0
Requires:       crate(getrandom-0.3/default) >= 0.3.0
Requires:       crate(indexmap-2/default) >= 2.2.3
Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(md-5-0.10/default) >= 0.10.0
Requires:       crate(nom-8/default) >= 8.0.0
Requires:       crate(nom-locate-5/default) >= 5.0.0
Requires:       crate(rand-0.9/default) >= 0.9.0
Requires:       crate(rangemap-1/default) >= 1.5.0
Requires:       crate(sha2-0.10/default) >= 0.10.8
Requires:       crate(stringprep-0.1/default) >= 0.1.5
Requires:       crate(thiserror-2/default) >= 2.0.3
Requires:       crate(ttf-parser-0.25/default) >= 0.25.1
Requires:       crate(weezl-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "lopdf"

%package     -n %{name}+async
Summary:        PDF document manipulation - feature "async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.0.0
Provides:       crate(%{pkgname}/async) = %{version}

%description -n %{name}+async
This metapackage enables feature "async" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        PDF document manipulation - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.0
Requires:       crate(chrono-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        PDF document manipulation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/jiff) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+image
Summary:        PDF document manipulation - feature "image" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(image-0.25/default) >= 0.25.0
Provides:       crate(%{pkgname}/embed-image) = %{version}
Provides:       crate(%{pkgname}/image) = %{version}

%description -n %{name}+image
This metapackage enables feature "image" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "embed_image" feature.

%package     -n %{name}+jiff
Summary:        PDF document manipulation - feature "jiff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/jiff) = %{version}

%description -n %{name}+jiff
This metapackage enables feature "jiff" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        PDF document manipulation - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.6.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        PDF document manipulation - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        PDF document manipulation - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/default) >= 0.3.0
Requires:       crate(time-0.3/formatting) >= 0.3.0
Requires:       crate(time-0.3/parsing) >= 0.3.0
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        PDF document manipulation - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wasm-js
Summary:        PDF document manipulation - feature "wasm_js"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.0
Provides:       crate(%{pkgname}/wasm-js) = %{version}

%description -n %{name}+wasm-js
This metapackage enables feature "wasm_js" for the Rust lopdf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

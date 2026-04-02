# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name time
%global full_version 0.3.47
%global pkgname time-0.3

Name:           rust-time-0.3
Version:        0.3.47
Release:        %autorelease
Summary:        Rust crate "time"
License:        MIT OR Apache-2.0
URL:            https://time-rs.github.io
#!RemoteAsset:  sha256:743bd48c283afc0388f9b8827b976905fb217ad9e647fae3a379a9283c4def2c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(deranged-0.5/default) >= 0.5.8
Requires:       crate(deranged-0.5/powerfmt) >= 0.5.8
Requires:       crate(num-conv-0.2/default) >= 0.2.1
Requires:       crate(powerfmt-0.2) >= 0.2.0
Requires:       crate(time-core-0.1/default) >= 0.1.8
Provides:       crate(%{pkgname})

%description
Fully interoperable with the standard library. Mostly compatible with #![no_std].
Source code for takopackized Rust crate "time"

%package     -n %{name}+alloc
Summary:        Date and time library - feature "alloc" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/alloc) >= 1.0.228
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+alloc
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "alloc" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "std" features.

%package     -n %{name}+formatting
Summary:        Date and time library - feature "formatting"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(itoa-1.0/default) >= 1.0.18
Requires:       crate(time-macros-0.2/formatting) >= 0.2.27
Provides:       crate(%{pkgname}/formatting)

%description -n %{name}+formatting
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "formatting" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+large-dates
Summary:        Date and time library - feature "large-dates"
Requires:       crate(%{pkgname})
Requires:       crate(time-core-0.1/large-dates) >= 0.1.8
Requires:       crate(time-macros-0.2/large-dates) >= 0.2.27
Provides:       crate(%{pkgname}/large-dates)

%description -n %{name}+large-dates
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "large-dates" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+local-offset
Summary:        Date and time library - feature "local-offset"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(libc-0.2/default) >= 0.2.98
Requires:       crate(num-threads-0.1/default) >= 0.1.2
Provides:       crate(%{pkgname}/local-offset)

%description -n %{name}+local-offset
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "local-offset" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Date and time library - feature "macros"
Requires:       crate(%{pkgname})
Requires:       crate(time-macros-0.2/default) >= 0.2.27
Provides:       crate(%{pkgname}/macros)

%description -n %{name}+macros
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "macros" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parsing
Summary:        Date and time library - feature "parsing"
Requires:       crate(%{pkgname})
Requires:       crate(time-macros-0.2/parsing) >= 0.2.27
Provides:       crate(%{pkgname}/parsing)

%description -n %{name}+parsing
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "parsing" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Date and time library - feature "quickcheck"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(deranged-0.5/powerfmt) >= 0.5.8
Requires:       crate(deranged-0.5/quickcheck) >= 0.5.8
Requires:       crate(quickcheck-1.0) >= 1.0.3
Provides:       crate(%{pkgname}/quickcheck)

%description -n %{name}+quickcheck
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "quickcheck" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Date and time library - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rand08)
Requires:       crate(%{pkgname}/rand09)
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "rand" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand08
Summary:        Date and time library - feature "rand08"
Requires:       crate(%{pkgname})
Requires:       crate(deranged-0.5/powerfmt) >= 0.5.8
Requires:       crate(deranged-0.5/rand08) >= 0.5.8
Requires:       crate(rand-0.8) >= 0.8.4
Provides:       crate(%{pkgname}/rand08)

%description -n %{name}+rand08
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "rand08" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand09
Summary:        Date and time library - feature "rand09"
Requires:       crate(%{pkgname})
Requires:       crate(deranged-0.5/powerfmt) >= 0.5.8
Requires:       crate(deranged-0.5/rand09) >= 0.5.8
Requires:       crate(rand-0.9) >= 0.9.2
Provides:       crate(%{pkgname}/rand09)

%description -n %{name}+rand09
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "rand09" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Date and time library - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(deranged-0.5/powerfmt) >= 0.5.8
Requires:       crate(deranged-0.5/serde) >= 0.5.8
Requires:       crate(serde-core-1.0) >= 1.0.228
Requires:       crate(time-macros-0.2/serde) >= 0.2.27
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "serde" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-human-readable
Summary:        Date and time library - feature "serde-human-readable" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/formatting)
Requires:       crate(%{pkgname}/parsing)
Requires:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/serde-human-readable)
Provides:       crate(%{pkgname}/serde-well-known)

%description -n %{name}+serde-human-readable
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "serde-human-readable" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde-well-known" feature.

%package     -n %{name}+wasm-bindgen
Summary:        Date and time library - feature "wasm-bindgen"
Requires:       crate(%{pkgname})
Requires:       crate(js-sys-0.3/default) >= 0.3.58
Provides:       crate(%{pkgname}/wasm-bindgen)

%description -n %{name}+wasm-bindgen
Fully interoperable with the standard library. Mostly compatible with #![no_std].
This metapackage enables feature "wasm-bindgen" for the Rust time crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

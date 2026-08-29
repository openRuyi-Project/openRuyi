# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name usvg
%global full_version 0.45.1
%global pkgname usvg-0.45

Name:           rust-usvg-0.45
Version:        0.45.1
Release:        %autorelease
Summary:        Rust crate "usvg"
License:        Apache-2.0 OR MIT
URL:            https://github.com/linebender/resvg
#!RemoteAsset:  sha256:80be9b06fbae3b8b303400ab20778c80bbaf338f563afe567cf3c9eea17b47ef
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(data-url-0.3/default) >= 0.3.0
Requires:       crate(flate2-1/rust-backend) >= 1.0.0
Requires:       crate(imagesize-0.13/default) >= 0.13.0
Requires:       crate(kurbo-0.11/default) >= 0.11.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(pico-args-0.5/default) >= 0.5.0
Requires:       crate(pico-args-0.5/eq-separator) >= 0.5.0
Requires:       crate(roxmltree-0.20/default) >= 0.20.0
Requires:       crate(simplecss-0.2/default) >= 0.2.0
Requires:       crate(siphasher-1/default) >= 1.0.0
Requires:       crate(strict-num-0.1/default) >= 0.1.1
Requires:       crate(svgtypes-0.15/default) >= 0.15.3
Requires:       crate(tiny-skia-path-0.11/default) >= 0.11.4
Requires:       crate(xmlwriter-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "usvg"

%package     -n %{name}+default
Summary:        SVG simplification library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/memmap-fonts) = %{version}
Requires:       crate(%{pkgname}/system-fonts) = %{version}
Requires:       crate(%{pkgname}/text) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust usvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fontdb
Summary:        SVG simplification library - feature "fontdb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fontdb-0.23) >= 0.23.0
Provides:       crate(%{pkgname}/fontdb) = %{version}

%description -n %{name}+fontdb
This metapackage enables feature "fontdb" for the Rust usvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memmap-fonts
Summary:        SVG simplification library - feature "memmap-fonts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fontdb-0.23/memmap) >= 0.23.0
Provides:       crate(%{pkgname}/memmap-fonts) = %{version}

%description -n %{name}+memmap-fonts
This metapackage enables feature "memmap-fonts" for the Rust usvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustybuzz
Summary:        SVG simplification library - feature "rustybuzz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustybuzz-0.20/default) >= 0.20.1
Provides:       crate(%{pkgname}/rustybuzz) = %{version}

%description -n %{name}+rustybuzz
This metapackage enables feature "rustybuzz" for the Rust usvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system-fonts
Summary:        SVG simplification library - feature "system-fonts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fontdb-0.23/fontconfig) >= 0.23.0
Requires:       crate(fontdb-0.23/fs) >= 0.23.0
Provides:       crate(%{pkgname}/system-fonts) = %{version}

%description -n %{name}+system-fonts
This metapackage enables feature "system-fonts" for the Rust usvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+text
Summary:        SVG simplification library - feature "text"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fontdb) = %{version}
Requires:       crate(%{pkgname}/rustybuzz) = %{version}
Requires:       crate(%{pkgname}/unicode-bidi) = %{version}
Requires:       crate(%{pkgname}/unicode-script) = %{version}
Requires:       crate(%{pkgname}/unicode-vo) = %{version}
Provides:       crate(%{pkgname}/text) = %{version}

%description -n %{name}+text
This metapackage enables feature "text" for the Rust usvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-bidi
Summary:        SVG simplification library - feature "unicode-bidi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-bidi-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/unicode-bidi) = %{version}

%description -n %{name}+unicode-bidi
This metapackage enables feature "unicode-bidi" for the Rust usvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-script
Summary:        SVG simplification library - feature "unicode-script"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-script-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/unicode-script) = %{version}

%description -n %{name}+unicode-script
This metapackage enables feature "unicode-script" for the Rust usvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-vo
Summary:        SVG simplification library - feature "unicode-vo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-vo-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/unicode-vo) = %{version}

%description -n %{name}+unicode-vo
This metapackage enables feature "unicode-vo" for the Rust usvg crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

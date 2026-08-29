# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name resvg
%global full_version 0.45.1
%global pkgname resvg-0.45

Name:           rust-resvg-0.45
Version:        0.45.1
Release:        %autorelease
Summary:        Rust crate "resvg"
License:        Apache-2.0 OR MIT
URL:            https://github.com/linebender/resvg
#!RemoteAsset:  sha256:a8928798c0a55e03c9ca6c4c6846f76377427d2c1e1f7e6de3c06ae57942df43
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(pico-args-0.5/default) >= 0.5.0
Requires:       crate(pico-args-0.5/eq-separator) >= 0.5.0
Requires:       crate(rgb-0.8/default) >= 0.8.0
Requires:       crate(svgtypes-0.15/default) >= 0.15.3
Requires:       crate(tiny-skia-0.11/default) >= 0.11.4
Requires:       crate(usvg-0.45) >= 0.45.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "resvg"

%package     -n %{name}+default
Summary:        SVG rendering library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/memmap-fonts) = %{version}
Requires:       crate(%{pkgname}/raster-images) = %{version}
Requires:       crate(%{pkgname}/system-fonts) = %{version}
Requires:       crate(%{pkgname}/text) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust resvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gif
Summary:        SVG rendering library - feature "gif"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gif-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/gif) = %{version}

%description -n %{name}+gif
This metapackage enables feature "gif" for the Rust resvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+image-webp
Summary:        SVG rendering library - feature "image-webp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(image-webp-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/image-webp) = %{version}

%description -n %{name}+image-webp
This metapackage enables feature "image-webp" for the Rust resvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memmap-fonts
Summary:        SVG rendering library - feature "memmap-fonts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(usvg-0.45/memmap-fonts) >= 0.45.1
Provides:       crate(%{pkgname}/memmap-fonts) = %{version}

%description -n %{name}+memmap-fonts
This metapackage enables feature "memmap-fonts" for the Rust resvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+raster-images
Summary:        SVG rendering library - feature "raster-images"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gif) = %{version}
Requires:       crate(%{pkgname}/image-webp) = %{version}
Requires:       crate(zune-jpeg-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/raster-images) = %{version}

%description -n %{name}+raster-images
This metapackage enables feature "raster-images" for the Rust resvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system-fonts
Summary:        SVG rendering library - feature "system-fonts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(usvg-0.45/system-fonts) >= 0.45.1
Provides:       crate(%{pkgname}/system-fonts) = %{version}

%description -n %{name}+system-fonts
This metapackage enables feature "system-fonts" for the Rust resvg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+text
Summary:        SVG rendering library - feature "text"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(usvg-0.45/text) >= 0.45.1
Provides:       crate(%{pkgname}/text) = %{version}

%description -n %{name}+text
This metapackage enables feature "text" for the Rust resvg crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

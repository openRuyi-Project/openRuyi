# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name plotters
%global full_version 0.3.7
%global pkgname plotters-0.3

Name:           rust-plotters-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "plotters"
License:        MIT
URL:            https://plotters-rs.github.io/
#!RemoteAsset:  sha256:5aeb6f403d7a4911efb1e33402027fc44f29b5bf6def3effcc22d7bb75f2b747
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/default) >= 0.2.14
Requires:       crate(plotters-backend-0.3/default) >= 0.3.6
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.89
Requires:       crate(web-sys-0.3/canvasrenderingcontext2d) >= 0.3.66
Requires:       crate(web-sys-0.3/default) >= 0.3.66
Requires:       crate(web-sys-0.3/document) >= 0.3.66
Requires:       crate(web-sys-0.3/domrect) >= 0.3.66
Requires:       crate(web-sys-0.3/element) >= 0.3.66
Requires:       crate(web-sys-0.3/htmlcanvaselement) >= 0.3.66
Requires:       crate(web-sys-0.3/htmlelement) >= 0.3.66
Requires:       crate(web-sys-0.3/node) >= 0.3.66
Requires:       crate(web-sys-0.3/window) >= 0.3.66
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/area-series) = %{version}
Provides:       crate(%{pkgname}/boxplot) = %{version}
Provides:       crate(%{pkgname}/candlestick) = %{version}
Provides:       crate(%{pkgname}/colormaps) = %{version}
Provides:       crate(%{pkgname}/deprecated-items) = %{version}
Provides:       crate(%{pkgname}/errorbar) = %{version}
Provides:       crate(%{pkgname}/full-palette) = %{version}
Provides:       crate(%{pkgname}/histogram) = %{version}
Provides:       crate(%{pkgname}/line-series) = %{version}
Provides:       crate(%{pkgname}/point-series) = %{version}
Provides:       crate(%{pkgname}/surface-series) = %{version}

%description
Source code for takopackized Rust crate "plotters"

%package     -n %{name}+ab-glyph
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "ab_glyph"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Requires:       crate(ab-glyph-0.2/default) >= 0.2.12
Provides:       crate(%{pkgname}/ab-glyph) = %{version}

%description -n %{name}+ab-glyph
This metapackage enables feature "ab_glyph" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-elements
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "all_elements"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/boxplot) = %{version}
Requires:       crate(%{pkgname}/candlestick) = %{version}
Requires:       crate(%{pkgname}/errorbar) = %{version}
Requires:       crate(%{pkgname}/histogram) = %{version}
Provides:       crate(%{pkgname}/all-elements) = %{version}

%description -n %{name}+all-elements
This metapackage enables feature "all_elements" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-series
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "all_series"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/area-series) = %{version}
Requires:       crate(%{pkgname}/line-series) = %{version}
Requires:       crate(%{pkgname}/point-series) = %{version}
Requires:       crate(%{pkgname}/surface-series) = %{version}
Provides:       crate(%{pkgname}/all-series) = %{version}

%description -n %{name}+all-series
This metapackage enables feature "all_series" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitmap-encoder
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "bitmap_encoder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(plotters-bitmap-0.3/image-encoder) >= 0.3.6
Provides:       crate(%{pkgname}/bitmap-encoder) = %{version}

%description -n %{name}+bitmap-encoder
This metapackage enables feature "bitmap_encoder" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitmap-gif
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "bitmap_gif"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(plotters-bitmap-0.3/gif-backend) >= 0.3.6
Provides:       crate(%{pkgname}/bitmap-gif) = %{version}

%description -n %{name}+bitmap-gif
This metapackage enables feature "bitmap_gif" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "chrono" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.32
Provides:       crate(%{pkgname}/chrono) = %{version}
Provides:       crate(%{pkgname}/datetime) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "datetime" feature.

%package     -n %{name}+default
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/all-elements) = %{version}
Requires:       crate(%{pkgname}/all-series) = %{version}
Requires:       crate(%{pkgname}/bitmap-backend) = %{version}
Requires:       crate(%{pkgname}/bitmap-encoder) = %{version}
Requires:       crate(%{pkgname}/bitmap-gif) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/colormaps) = %{version}
Requires:       crate(%{pkgname}/deprecated-items) = %{version}
Requires:       crate(%{pkgname}/full-palette) = %{version}
Requires:       crate(%{pkgname}/image) = %{version}
Requires:       crate(%{pkgname}/svg-backend) = %{version}
Requires:       crate(%{pkgname}/ttf) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+evcxr-bitmap
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "evcxr_bitmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitmap-backend) = %{version}
Requires:       crate(%{pkgname}/evcxr) = %{version}
Requires:       crate(plotters-svg-0.3/bitmap-encoder) >= 0.3.6
Provides:       crate(%{pkgname}/evcxr-bitmap) = %{version}

%description -n %{name}+evcxr-bitmap
This metapackage enables feature "evcxr_bitmap" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+font-kit
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "font-kit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(font-kit-0.14/default) >= 0.14.2
Provides:       crate(%{pkgname}/font-kit) = %{version}

%description -n %{name}+font-kit
This metapackage enables feature "font-kit" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fontconfig-dlopen
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "fontconfig-dlopen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(font-kit-0.14/source-fontconfig-dlopen) >= 0.14.2
Provides:       crate(%{pkgname}/fontconfig-dlopen) = %{version}

%description -n %{name}+fontconfig-dlopen
This metapackage enables feature "fontconfig-dlopen" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+image
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "image"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(image-0.24/bmp) >= 0.24.3
Requires:       crate(image-0.24/jpeg) >= 0.24.3
Requires:       crate(image-0.24/png) >= 0.24.3
Provides:       crate(%{pkgname}/image) = %{version}

%description -n %{name}+image
This metapackage enables feature "image" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lazy-static
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "lazy_static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lazy-static-1/default) >= 1.4.0
Provides:       crate(%{pkgname}/lazy-static) = %{version}

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pathfinder-geometry
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "pathfinder_geometry"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pathfinder-geometry-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}/pathfinder-geometry) = %{version}

%description -n %{name}+pathfinder-geometry
This metapackage enables feature "pathfinder_geometry" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+plotters-bitmap
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "plotters-bitmap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(plotters-bitmap-0.3) >= 0.3.6
Provides:       crate(%{pkgname}/bitmap-backend) = %{version}
Provides:       crate(%{pkgname}/plotters-bitmap) = %{version}

%description -n %{name}+plotters-bitmap
This metapackage enables feature "plotters-bitmap" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bitmap_backend" feature.

%package     -n %{name}+plotters-svg
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "plotters-svg" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(plotters-svg-0.3/default) >= 0.3.6
Provides:       crate(%{pkgname}/evcxr) = %{version}
Provides:       crate(%{pkgname}/plotters-svg) = %{version}
Provides:       crate(%{pkgname}/svg-backend) = %{version}

%description -n %{name}+plotters-svg
This metapackage enables feature "plotters-svg" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "evcxr", and "svg_backend" features.

%package     -n %{name}+ttf
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "ttf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/font-kit) = %{version}
Requires:       crate(%{pkgname}/lazy-static) = %{version}
Requires:       crate(%{pkgname}/pathfinder-geometry) = %{version}
Requires:       crate(%{pkgname}/ttf-parser) = %{version}
Provides:       crate(%{pkgname}/ttf) = %{version}

%description -n %{name}+ttf
This metapackage enables feature "ttf" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ttf-parser
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "ttf-parser"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ttf-parser-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/ttf-parser) = %{version}

%description -n %{name}+ttf-parser
This metapackage enables feature "ttf-parser" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

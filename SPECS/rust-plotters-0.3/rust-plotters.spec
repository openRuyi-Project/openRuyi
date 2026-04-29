# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(plotters-backend-0.3/default) >= 0.3.7
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.118
Requires:       crate(web-sys-0.3/canvasrenderingcontext2d) >= 0.3.95
Requires:       crate(web-sys-0.3/default) >= 0.3.95
Requires:       crate(web-sys-0.3/document) >= 0.3.95
Requires:       crate(web-sys-0.3/domrect) >= 0.3.95
Requires:       crate(web-sys-0.3/element) >= 0.3.95
Requires:       crate(web-sys-0.3/htmlcanvaselement) >= 0.3.95
Requires:       crate(web-sys-0.3/htmlelement) >= 0.3.95
Requires:       crate(web-sys-0.3/node) >= 0.3.95
Requires:       crate(web-sys-0.3/window) >= 0.3.95
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/area-series)
Provides:       crate(%{pkgname}/boxplot)
Provides:       crate(%{pkgname}/candlestick)
Provides:       crate(%{pkgname}/colormaps)
Provides:       crate(%{pkgname}/deprecated-items)
Provides:       crate(%{pkgname}/errorbar)
Provides:       crate(%{pkgname}/full-palette)
Provides:       crate(%{pkgname}/histogram)
Provides:       crate(%{pkgname}/line-series)
Provides:       crate(%{pkgname}/point-series)
Provides:       crate(%{pkgname}/surface-series)

%description
Source code for takopackized Rust crate "plotters"

%package     -n %{name}+ab-glyph
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "ab_glyph"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/once-cell)
Requires:       crate(ab-glyph-0.2/default) >= 0.2.12
Provides:       crate(%{pkgname}/ab-glyph)

%description -n %{name}+ab-glyph
This metapackage enables feature "ab_glyph" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-elements
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "all_elements"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/boxplot)
Requires:       crate(%{pkgname}/candlestick)
Requires:       crate(%{pkgname}/errorbar)
Requires:       crate(%{pkgname}/histogram)
Provides:       crate(%{pkgname}/all-elements)

%description -n %{name}+all-elements
This metapackage enables feature "all_elements" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-series
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "all_series"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/area-series)
Requires:       crate(%{pkgname}/line-series)
Requires:       crate(%{pkgname}/point-series)
Requires:       crate(%{pkgname}/surface-series)
Provides:       crate(%{pkgname}/all-series)

%description -n %{name}+all-series
This metapackage enables feature "all_series" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitmap-encoder
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "bitmap_encoder"
Requires:       crate(%{pkgname})
Requires:       crate(plotters-bitmap-0.3/image-encoder) >= 0.3.6
Provides:       crate(%{pkgname}/bitmap-encoder)

%description -n %{name}+bitmap-encoder
This metapackage enables feature "bitmap_encoder" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitmap-gif
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "bitmap_gif"
Requires:       crate(%{pkgname})
Requires:       crate(plotters-bitmap-0.3/gif-backend) >= 0.3.6
Provides:       crate(%{pkgname}/bitmap-gif)

%description -n %{name}+bitmap-gif
This metapackage enables feature "bitmap_gif" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "chrono" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(chrono-0.4/default) >= 0.4.32
Provides:       crate(%{pkgname}/chrono)
Provides:       crate(%{pkgname}/datetime)

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "datetime" feature.

%package     -n %{name}+default
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/all-elements)
Requires:       crate(%{pkgname}/all-series)
Requires:       crate(%{pkgname}/bitmap-backend)
Requires:       crate(%{pkgname}/bitmap-encoder)
Requires:       crate(%{pkgname}/bitmap-gif)
Requires:       crate(%{pkgname}/chrono)
Requires:       crate(%{pkgname}/colormaps)
Requires:       crate(%{pkgname}/deprecated-items)
Requires:       crate(%{pkgname}/full-palette)
Requires:       crate(%{pkgname}/image)
Requires:       crate(%{pkgname}/svg-backend)
Requires:       crate(%{pkgname}/ttf)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+evcxr-bitmap
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "evcxr_bitmap"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitmap-backend)
Requires:       crate(%{pkgname}/evcxr)
Requires:       crate(plotters-svg-0.3/bitmap-encoder) >= 0.3.7
Provides:       crate(%{pkgname}/evcxr-bitmap)

%description -n %{name}+evcxr-bitmap
This metapackage enables feature "evcxr_bitmap" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+font-kit
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "font-kit"
Requires:       crate(%{pkgname})
Requires:       crate(font-kit-0.14/default) >= 0.14.2
Provides:       crate(%{pkgname}/font-kit)

%description -n %{name}+font-kit
This metapackage enables feature "font-kit" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fontconfig-dlopen
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "fontconfig-dlopen"
Requires:       crate(%{pkgname})
Requires:       crate(font-kit-0.14/source-fontconfig-dlopen) >= 0.14.2
Provides:       crate(%{pkgname}/fontconfig-dlopen)

%description -n %{name}+fontconfig-dlopen
This metapackage enables feature "fontconfig-dlopen" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+image
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "image"
Requires:       crate(%{pkgname})
Requires:       crate(image-0.24/bmp) >= 0.24.3
Requires:       crate(image-0.24/jpeg) >= 0.24.3
Requires:       crate(image-0.24/png) >= 0.24.3
Provides:       crate(%{pkgname}/image)

%description -n %{name}+image
This metapackage enables feature "image" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lazy-static
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "lazy_static"
Requires:       crate(%{pkgname})
Requires:       crate(lazy-static-1.0/default) >= 1.4.0
Provides:       crate(%{pkgname}/lazy-static)

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "once_cell"
Requires:       crate(%{pkgname})
Requires:       crate(once-cell-1.0/default) >= 1.8.0
Provides:       crate(%{pkgname}/once-cell)

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pathfinder-geometry
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "pathfinder_geometry"
Requires:       crate(%{pkgname})
Requires:       crate(pathfinder-geometry-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}/pathfinder-geometry)

%description -n %{name}+pathfinder-geometry
This metapackage enables feature "pathfinder_geometry" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+plotters-bitmap
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "plotters-bitmap" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(plotters-bitmap-0.3) >= 0.3.6
Provides:       crate(%{pkgname}/bitmap-backend)
Provides:       crate(%{pkgname}/plotters-bitmap)

%description -n %{name}+plotters-bitmap
This metapackage enables feature "plotters-bitmap" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bitmap_backend" feature.

%package     -n %{name}+plotters-svg
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "plotters-svg" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(plotters-svg-0.3/default) >= 0.3.7
Provides:       crate(%{pkgname}/evcxr)
Provides:       crate(%{pkgname}/plotters-svg)
Provides:       crate(%{pkgname}/svg-backend)

%description -n %{name}+plotters-svg
This metapackage enables feature "plotters-svg" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "evcxr", and "svg_backend" features.

%package     -n %{name}+ttf
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "ttf"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/font-kit)
Requires:       crate(%{pkgname}/lazy-static)
Requires:       crate(%{pkgname}/pathfinder-geometry)
Requires:       crate(%{pkgname}/ttf-parser)
Provides:       crate(%{pkgname}/ttf)

%description -n %{name}+ttf
This metapackage enables feature "ttf" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ttf-parser
Summary:        Rust drawing library focus on data plotting for both WASM and native applications - feature "ttf-parser"
Requires:       crate(%{pkgname})
Requires:       crate(ttf-parser-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/ttf-parser)

%description -n %{name}+ttf-parser
This metapackage enables feature "ttf-parser" for the Rust plotters crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

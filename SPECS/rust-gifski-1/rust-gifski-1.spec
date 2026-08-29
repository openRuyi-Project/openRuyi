# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gifski
%global full_version 1.34.0
%global pkgname gifski-1

Name:           rust-gifski-1
Version:        1.34.0
Release:        %autorelease
Summary:        Rust crate "gifski"
License:        AGPL-3.0-or-later
URL:            https://gif.ski
#!RemoteAsset:  sha256:c246c795a61d4a2476fb1c8ab70bedfaa825c734882adc40e117fc837df81190
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.14
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.21
Requires:       crate(gif-0.13/raii-no-panic) >= 0.13.1
Requires:       crate(gif-0.13/std) >= 0.13.1
Requires:       crate(gif-dispose-5/default) >= 5.0.1
Requires:       crate(imagequant-4/default) >= 4.3.4
Requires:       crate(imgref-1/default) >= 1.11.0
Requires:       crate(loop9-0.1/default) >= 0.1.5
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(ordered-channel-1/crossbeam-channel) >= 1.2.0
Requires:       crate(ordered-channel-1/default) >= 1.2.0
Requires:       crate(quick-error-2/default) >= 2.0.1
Requires:       crate(resize-0.8/default) >= 0.8.8
Requires:       crate(resize-0.8/rayon) >= 0.8.8
Requires:       crate(rgb-0.8/bytemuck) >= 0.8.50

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/capi) = %{version}
Provides:       crate(%{pkgname}/gifsicle) = %{version}

%description
Source code for takopackized Rust crate "gifski"

%package     -n %{name}+binary
Summary:        Pngquant-based GIF maker for nice-looking animGIFs - feature "binary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pbr) = %{version}
Requires:       crate(%{pkgname}/png) = %{version}
Requires:       crate(clap-4/cargo) >= 4.5.32
Requires:       crate(clap-4/default) >= 4.5.32
Requires:       crate(dunce-1/default) >= 1.0.5
Requires:       crate(natord-1/default) >= 1.0.9
Requires:       crate(wild-2/default) >= 2.2.1
Requires:       crate(wild-2/glob-quoted-on-windows) >= 2.2.1
Requires:       crate(y4m-0.8/default) >= 0.8.0
Requires:       crate(yuv-0.1/default) >= 0.1.9
Provides:       crate(%{pkgname}/binary) = %{version}

%description -n %{name}+binary
This metapackage enables feature "binary" for the Rust gifski crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pngquant-based GIF maker for nice-looking animGIFs - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/binary) = %{version}
Requires:       crate(%{pkgname}/gifsicle) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gifski crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pbr
Summary:        Pngquant-based GIF maker for nice-looking animGIFs - feature "pbr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pbr-1/default) >= 1.1.1
Provides:       crate(%{pkgname}/pbr) = %{version}

%description -n %{name}+pbr
This metapackage enables feature "pbr" for the Rust gifski crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+png
Summary:        Pngquant-based GIF maker for nice-looking animGIFs - feature "png"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lodepng-3/default) >= 3.11.0
Provides:       crate(%{pkgname}/png) = %{version}

%description -n %{name}+png
This metapackage enables feature "png" for the Rust gifski crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+video
Summary:        Pngquant-based GIF maker for nice-looking animGIFs - feature "video"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ffmpeg-next-6/codec) >= 6.0.0
Requires:       crate(ffmpeg-next-6/filter) >= 6.0.0
Requires:       crate(ffmpeg-next-6/format) >= 6.0.0
Requires:       crate(ffmpeg-next-6/software-resampling) >= 6.0.0
Requires:       crate(ffmpeg-next-6/software-scaling) >= 6.0.0
Provides:       crate(%{pkgname}/video) = %{version}

%description -n %{name}+video
This metapackage enables feature "video" for the Rust gifski crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+video-prebuilt-static
Summary:        Pngquant-based GIF maker for nice-looking animGIFs - feature "video-prebuilt-static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/video) = %{version}
Requires:       crate(ffmpeg-next-6/codec) >= 6.0.0
Requires:       crate(ffmpeg-next-6/filter) >= 6.0.0
Requires:       crate(ffmpeg-next-6/format) >= 6.0.0
Requires:       crate(ffmpeg-next-6/software-resampling) >= 6.0.0
Requires:       crate(ffmpeg-next-6/software-scaling) >= 6.0.0
Requires:       crate(ffmpeg-next-6/static) >= 6.0.0
Provides:       crate(%{pkgname}/video-prebuilt-static) = %{version}

%description -n %{name}+video-prebuilt-static
This metapackage enables feature "video-prebuilt-static" for the Rust gifski crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+video-static
Summary:        Pngquant-based GIF maker for nice-looking animGIFs - feature "video-static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/video) = %{version}
Requires:       crate(ffmpeg-next-6/build) >= 6.0.0
Requires:       crate(ffmpeg-next-6/codec) >= 6.0.0
Requires:       crate(ffmpeg-next-6/filter) >= 6.0.0
Requires:       crate(ffmpeg-next-6/format) >= 6.0.0
Requires:       crate(ffmpeg-next-6/software-resampling) >= 6.0.0
Requires:       crate(ffmpeg-next-6/software-scaling) >= 6.0.0
Provides:       crate(%{pkgname}/video-static) = %{version}

%description -n %{name}+video-static
This metapackage enables feature "video-static" for the Rust gifski crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

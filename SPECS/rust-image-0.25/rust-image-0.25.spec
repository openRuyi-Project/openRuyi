# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name image
%global full_version 0.25.10
%global pkgname image-0.25

Name:           rust-image-0.25
Version:        0.25.10
Release:        %autorelease
Summary:        Rust crate "image"
License:        MIT OR Apache-2.0
URL:            https://github.com/image-rs/image
#!RemoteAsset:  sha256:85ab80394333c02fe689eaf900ab500fbd0c2213da414687ebf995a65d5a6104
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytemuck-1/default) >= 1.8.0
Requires:       crate(bytemuck-1/extern-crate-alloc) >= 1.8.0
Requires:       crate(byteorder-lite-0.1/default) >= 0.1.0
Requires:       crate(moxcms-0.8/default) >= 0.8.0
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/benchmarks) = %{version}
Provides:       crate(%{pkgname}/bmp) = %{version}
Provides:       crate(%{pkgname}/dds) = %{version}
Provides:       crate(%{pkgname}/ff) = %{version}
Provides:       crate(%{pkgname}/hdr) = %{version}
Provides:       crate(%{pkgname}/pnm) = %{version}
Provides:       crate(%{pkgname}/tga) = %{version}

%description
Provides basic image processing and encoders/decoders for common image formats.
Source code for takopackized Rust crate "image"

%package     -n %{name}+avif
Summary:        Imaging library - feature "avif"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ravif-0.13) >= 0.13.0
Requires:       crate(rgb-0.8) >= 0.8.48
Provides:       crate(%{pkgname}/avif) = %{version}

%description -n %{name}+avif
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "avif" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+avif-native
Summary:        Imaging library - feature "avif-native"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dav1d-0.11/default) >= 0.11.0
Requires:       crate(mp4parse-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/avif-native) = %{version}

%description -n %{name}+avif-native
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "avif-native" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color-quant
Summary:        Imaging library - feature "color_quant"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(color-quant-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/color-quant) = %{version}

%description -n %{name}+color-quant
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "color_quant" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Imaging library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/default-formats) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "default" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default-formats
Summary:        Imaging library - feature "default-formats"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/avif) = %{version}
Requires:       crate(%{pkgname}/bmp) = %{version}
Requires:       crate(%{pkgname}/dds) = %{version}
Requires:       crate(%{pkgname}/exr) = %{version}
Requires:       crate(%{pkgname}/ff) = %{version}
Requires:       crate(%{pkgname}/gif) = %{version}
Requires:       crate(%{pkgname}/hdr) = %{version}
Requires:       crate(%{pkgname}/ico) = %{version}
Requires:       crate(%{pkgname}/jpeg) = %{version}
Requires:       crate(%{pkgname}/png) = %{version}
Requires:       crate(%{pkgname}/pnm) = %{version}
Requires:       crate(%{pkgname}/qoi) = %{version}
Requires:       crate(%{pkgname}/tga) = %{version}
Requires:       crate(%{pkgname}/tiff) = %{version}
Requires:       crate(%{pkgname}/webp) = %{version}
Provides:       crate(%{pkgname}/default-formats) = %{version}

%description -n %{name}+default-formats
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "default-formats" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+exr
Summary:        Imaging library - feature "exr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(exr-1) >= 1.74.0
Provides:       crate(%{pkgname}/exr) = %{version}

%description -n %{name}+exr
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "exr" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gif
Summary:        Imaging library - feature "gif"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(color-quant-1/default) >= 1.1.0
Requires:       crate(gif-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/gif) = %{version}

%description -n %{name}+gif
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "gif" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ico
Summary:        Imaging library - feature "ico"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bmp) = %{version}
Requires:       crate(%{pkgname}/png) = %{version}
Provides:       crate(%{pkgname}/ico) = %{version}

%description -n %{name}+ico
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "ico" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jpeg
Summary:        Imaging library - feature "jpeg"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zune-core-0.5) >= 0.5.0
Requires:       crate(zune-jpeg-0.5/default) >= 0.5.5
Provides:       crate(%{pkgname}/jpeg) = %{version}

%description -n %{name}+jpeg
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "jpeg" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nasm
Summary:        Imaging library - feature "nasm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ravif-0.13/asm) >= 0.13.0
Provides:       crate(%{pkgname}/nasm) = %{version}

%description -n %{name}+nasm
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "nasm" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+png
Summary:        Imaging library - feature "png"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(png-0.18/default) >= 0.18.0
Provides:       crate(%{pkgname}/png) = %{version}

%description -n %{name}+png
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "png" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+qoi
Summary:        Imaging library - feature "qoi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(qoi-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/qoi) = %{version}

%description -n %{name}+qoi
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "qoi" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Imaging library - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(exr-1/rayon) >= 1.74.0
Requires:       crate(ravif-0.13/threading) >= 0.13.0
Requires:       crate(rayon-1/default) >= 1.7.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "rayon" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Imaging library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.214
Requires:       crate(serde-1/derive) >= 1.0.214
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "serde" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tiff
Summary:        Imaging library - feature "tiff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tiff-0.11/default) >= 0.11.2
Provides:       crate(%{pkgname}/tiff) = %{version}

%description -n %{name}+tiff
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "tiff" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webp
Summary:        Imaging library - feature "webp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(image-webp-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/webp) = %{version}

%description -n %{name}+webp
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "webp" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

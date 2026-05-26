# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name av-scenechange
%global full_version 0.14.1
%global pkgname av-scenechange-0.14

Name:           rust-av-scenechange-0.14
Version:        0.14.1
Release:        %autorelease
Summary:        Rust crate "av-scenechange"
License:        MIT
URL:            https://github.com/rust-av/av-scenechange
#!RemoteAsset:  sha256:0f321d77c20e19b92c39e7471cf986812cbb46659d2af674adc4331ef3f18394
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aligned-0.4/default) >= 0.4.3
Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(arg-enum-proc-macro-0.3/default) >= 0.3.4
Requires:       crate(arrayvec-0.7/default) >= 0.7.6
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(num-rational-0.4) >= 0.4.2
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(pastey-0.1/default) >= 0.1.1
Requires:       crate(rayon-1.0/default) >= 1.12.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(v-frame-0.3/default) >= 0.3.9
Requires:       crate(y4m-0.8/default) >= 0.8.0
Provides:       crate(av-scenechange) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "av-scenechange"

%package     -n %{name}+asm
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "asm"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cc)
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/nasm-rs)
Provides:       crate(%{pkgname}/asm)

%description -n %{name}+asm
This metapackage enables feature "asm" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+binary
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "binary"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/clap)
Requires:       crate(%{pkgname}/serialize)
Provides:       crate(%{pkgname}/binary)

%description -n %{name}+binary
This metapackage enables feature "binary" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cc
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "cc"
Requires:       crate(%{pkgname})
Requires:       crate(cc-1.0/default) >= 1.2.23
Requires:       crate(cc-1.0/parallel) >= 1.2.23
Provides:       crate(%{pkgname}/cc)

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "clap"
Requires:       crate(%{pkgname})
Requires:       crate(clap-4.0/default) >= 4.0.22
Requires:       crate(clap-4.0/derive) >= 4.0.22
Provides:       crate(%{pkgname}/clap)

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+console
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "console"
Requires:       crate(%{pkgname})
Requires:       crate(console-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/console)

%description -n %{name}+console
This metapackage enables feature "console" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/asm)
Requires:       crate(%{pkgname}/binary)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+devel
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "devel"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/console)
Requires:       crate(%{pkgname}/fern)
Provides:       crate(%{pkgname}/devel)

%description -n %{name}+devel
This metapackage enables feature "devel" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fern
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "fern"
Requires:       crate(%{pkgname})
Requires:       crate(fern-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/fern)

%description -n %{name}+fern
This metapackage enables feature "fern" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ffmpeg-the-third
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "ffmpeg-the-third" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(ffmpeg-the-third-3.0/codec) >= 3.0.0
Requires:       crate(ffmpeg-the-third-3.0/format) >= 3.0.0
Provides:       crate(%{pkgname}/ffmpeg)
Provides:       crate(%{pkgname}/ffmpeg-the-third)

%description -n %{name}+ffmpeg-the-third
This metapackage enables feature "ffmpeg-the-third" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ffmpeg" feature.

%package     -n %{name}+libc
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2/default) >= 0.2.172
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nasm-rs
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "nasm-rs"
Requires:       crate(%{pkgname})
Requires:       crate(nasm-rs-0.3/default) >= 0.3.0
Requires:       crate(nasm-rs-0.3/parallel) >= 0.3.0
Provides:       crate(%{pkgname}/nasm-rs)

%description -n %{name}+nasm-rs
This metapackage enables feature "nasm-rs" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.123
Requires:       crate(serde-1.0/derive) >= 1.0.123
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "serde_json"
Requires:       crate(%{pkgname})
Requires:       crate(serde-json-1.0/default) >= 1.0.62
Provides:       crate(%{pkgname}/serde-json)

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialize
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "serialize"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/serde-json)
Provides:       crate(%{pkgname}/serialize)

%description -n %{name}+serialize
This metapackage enables feature "serialize" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/tracing-chrome)
Requires:       crate(%{pkgname}/tracing-subscriber)
Requires:       crate(tracing-0.1/default) >= 0.1.40
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-chrome
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "tracing-chrome"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-chrome-0.7/default) >= 0.7.1
Provides:       crate(%{pkgname}/tracing-chrome)

%description -n %{name}+tracing-chrome
This metapackage enables feature "tracing-chrome" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-subscriber
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "tracing-subscriber"
Requires:       crate(%{pkgname})
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.18
Provides:       crate(%{pkgname}/tracing-subscriber)

%description -n %{name}+tracing-subscriber
This metapackage enables feature "tracing-subscriber" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vapoursynth
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "vapoursynth"
Requires:       crate(%{pkgname})
Requires:       crate(vapoursynth-0.4/default) >= 0.4.0
Requires:       crate(vapoursynth-0.4/vapoursynth-api-32) >= 0.4.0
Requires:       crate(vapoursynth-0.4/vapoursynth-functions) >= 0.4.0
Requires:       crate(vapoursynth-0.4/vsscript-api-31) >= 0.4.0
Requires:       crate(vapoursynth-0.4/vsscript-functions) >= 0.4.0
Provides:       crate(%{pkgname}/vapoursynth)

%description -n %{name}+vapoursynth
This metapackage enables feature "vapoursynth" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

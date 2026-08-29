# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aligned-0.4/default) >= 0.4.2
Requires:       crate(anyhow-1/default) >= 1.0.56
Requires:       crate(arg-enum-proc-macro-0.3/default) >= 0.3.4
Requires:       crate(arrayvec-0.7/default) >= 0.7.6
Requires:       crate(log-0.4/default) >= 0.4.14
Requires:       crate(num-rational-0.4) >= 0.4.2
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(pastey-0.1/default) >= 0.1.0
Requires:       crate(rayon-1/default) >= 1.10.0
Requires:       crate(thiserror-2/default) >= 2.0.12
Requires:       crate(v-frame-0.3/default) >= 0.3.8
Requires:       crate(y4m-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "av-scenechange"

%package     -n %{name}+asm
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "asm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cc) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/nasm-rs) = %{version}
Provides:       crate(%{pkgname}/asm) = %{version}

%description -n %{name}+asm
This metapackage enables feature "asm" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+binary
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "binary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clap) = %{version}
Requires:       crate(%{pkgname}/serialize) = %{version}
Provides:       crate(%{pkgname}/binary) = %{version}

%description -n %{name}+binary
This metapackage enables feature "binary" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cc
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "cc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-1/default) >= 1.2.23
Requires:       crate(cc-1/parallel) >= 1.2.23
Provides:       crate(%{pkgname}/cc) = %{version}

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.0.22
Requires:       crate(clap-4/derive) >= 4.0.22
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+console
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "console"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(console-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/console) = %{version}

%description -n %{name}+console
This metapackage enables feature "console" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/asm) = %{version}
Requires:       crate(%{pkgname}/binary) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+devel
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "devel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/console) = %{version}
Requires:       crate(%{pkgname}/fern) = %{version}
Provides:       crate(%{pkgname}/devel) = %{version}

%description -n %{name}+devel
This metapackage enables feature "devel" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fern
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "fern"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fern-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/fern) = %{version}

%description -n %{name}+fern
This metapackage enables feature "fern" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ffmpeg-the-third
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "ffmpeg-the-third" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ffmpeg-the-third-3/codec) >= 3.0.0
Requires:       crate(ffmpeg-the-third-3/format) >= 3.0.0
Provides:       crate(%{pkgname}/ffmpeg) = %{version}
Provides:       crate(%{pkgname}/ffmpeg-the-third) = %{version}

%description -n %{name}+ffmpeg-the-third
This metapackage enables feature "ffmpeg-the-third" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ffmpeg" feature.

%package     -n %{name}+libc
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.172
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nasm-rs
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "nasm-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nasm-rs-0.3/default) >= 0.3.0
Requires:       crate(nasm-rs-0.3/parallel) >= 0.3.0
Provides:       crate(%{pkgname}/nasm-rs) = %{version}

%description -n %{name}+nasm-rs
This metapackage enables feature "nasm-rs" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.123
Requires:       crate(serde-1/derive) >= 1.0.123
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.62
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialize
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serialize
This metapackage enables feature "serialize" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tracing-chrome) = %{version}
Requires:       crate(%{pkgname}/tracing-subscriber) = %{version}
Requires:       crate(tracing-0.1/default) >= 0.1.40
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-chrome
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "tracing-chrome"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-chrome-0.7/default) >= 0.7.1
Provides:       crate(%{pkgname}/tracing-chrome) = %{version}

%description -n %{name}+tracing-chrome
This metapackage enables feature "tracing-chrome" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-subscriber
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "tracing-subscriber"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.18
Provides:       crate(%{pkgname}/tracing-subscriber) = %{version}

%description -n %{name}+tracing-subscriber
This metapackage enables feature "tracing-subscriber" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vapoursynth
Summary:        Estimates frames in a video where a scenecut would be ideal - feature "vapoursynth"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vapoursynth-0.4/default) >= 0.4.0
Requires:       crate(vapoursynth-0.4/vapoursynth-api-32) >= 0.4.0
Requires:       crate(vapoursynth-0.4/vapoursynth-functions) >= 0.4.0
Requires:       crate(vapoursynth-0.4/vsscript-api-31) >= 0.4.0
Requires:       crate(vapoursynth-0.4/vsscript-functions) >= 0.4.0
Provides:       crate(%{pkgname}/vapoursynth) = %{version}

%description -n %{name}+vapoursynth
This metapackage enables feature "vapoursynth" for the Rust av-scenechange crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

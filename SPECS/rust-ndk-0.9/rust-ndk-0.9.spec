# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ndk
%global full_version 0.9.0
%global pkgname ndk-0.9

Name:           rust-ndk-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "ndk"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-mobile/ndk
#!RemoteAsset:  sha256:c3f42e7bbe13d351b6bead8286a43aac9534b82bd3cc43e47037f012ebfd62d4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.0
Requires:       crate(jni-sys-0.3/default) >= 0.3.0
Requires:       crate(log-0.4/default) >= 0.4.6
Requires:       crate(ndk-sys-0.6/default) >= 0.6.0
Requires:       crate(num-enum-0.7/default) >= 0.7.0
Requires:       crate(thiserror-1/default) >= 1.0.23
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/api-level-23) = %{version}
Provides:       crate(%{pkgname}/api-level-24) = %{version}
Provides:       crate(%{pkgname}/api-level-25) = %{version}
Provides:       crate(%{pkgname}/api-level-26) = %{version}
Provides:       crate(%{pkgname}/api-level-27) = %{version}
Provides:       crate(%{pkgname}/api-level-28) = %{version}
Provides:       crate(%{pkgname}/api-level-29) = %{version}
Provides:       crate(%{pkgname}/api-level-30) = %{version}
Provides:       crate(%{pkgname}/api-level-31) = %{version}
Provides:       crate(%{pkgname}/api-level-32) = %{version}
Provides:       crate(%{pkgname}/api-level-33) = %{version}

%description
Source code for takopackized Rust crate "ndk"

%package     -n %{name}+all
Summary:        Safe Rust bindings to the Android NDK - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api-level-33) = %{version}
Requires:       crate(%{pkgname}/audio) = %{version}
Requires:       crate(%{pkgname}/bitmap) = %{version}
Requires:       crate(%{pkgname}/media) = %{version}
Requires:       crate(%{pkgname}/nativewindow) = %{version}
Requires:       crate(%{pkgname}/rwh-04) = %{version}
Requires:       crate(%{pkgname}/rwh-05) = %{version}
Requires:       crate(%{pkgname}/rwh-06) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+audio
Summary:        Safe Rust bindings to the Android NDK - feature "audio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api-level-26) = %{version}
Requires:       crate(ndk-sys-0.6/audio) >= 0.6.0
Provides:       crate(%{pkgname}/audio) = %{version}

%description -n %{name}+audio
This metapackage enables feature "audio" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitmap
Summary:        Safe Rust bindings to the Android NDK - feature "bitmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ndk-sys-0.6/bitmap) >= 0.6.0
Provides:       crate(%{pkgname}/bitmap) = %{version}

%description -n %{name}+bitmap
This metapackage enables feature "bitmap" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jni
Summary:        Safe Rust bindings to the Android NDK - feature "jni"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jni-0.21/default) >= 0.21.0
Provides:       crate(%{pkgname}/jni) = %{version}

%description -n %{name}+jni
This metapackage enables feature "jni" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+media
Summary:        Safe Rust bindings to the Android NDK - feature "media"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ndk-sys-0.6/media) >= 0.6.0
Provides:       crate(%{pkgname}/media) = %{version}

%description -n %{name}+media
This metapackage enables feature "media" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nativewindow
Summary:        Safe Rust bindings to the Android NDK - feature "nativewindow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ndk-sys-0.6/nativewindow) >= 0.6.0
Provides:       crate(%{pkgname}/nativewindow) = %{version}

%description -n %{name}+nativewindow
This metapackage enables feature "nativewindow" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rwh-04
Summary:        Safe Rust bindings to the Android NDK - feature "rwh_04"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(raw-window-handle-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/rwh-04) = %{version}

%description -n %{name}+rwh-04
This metapackage enables feature "rwh_04" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rwh-05
Summary:        Safe Rust bindings to the Android NDK - feature "rwh_05"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(raw-window-handle-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/rwh-05) = %{version}

%description -n %{name}+rwh-05
This metapackage enables feature "rwh_05" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rwh-06
Summary:        Safe Rust bindings to the Android NDK - feature "rwh_06" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(raw-window-handle-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rwh-06) = %{version}

%description -n %{name}+rwh-06
This metapackage enables feature "rwh_06" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+sync
Summary:        Safe Rust bindings to the Android NDK - feature "sync"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/api-level-26) = %{version}
Requires:       crate(ndk-sys-0.6/sync) >= 0.6.0
Provides:       crate(%{pkgname}/sync) = %{version}

%description -n %{name}+sync
This metapackage enables feature "sync" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test
Summary:        Safe Rust bindings to the Android NDK - feature "test"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/all) = %{version}
Requires:       crate(%{pkgname}/jni) = %{version}
Requires:       crate(ndk-sys-0.6/test) >= 0.6.0
Provides:       crate(%{pkgname}/test) = %{version}

%description -n %{name}+test
This metapackage enables feature "test" for the Rust ndk crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

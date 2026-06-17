# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gio
%global full_version 0.22.6
%global pkgname gio-0.22

Name:           rust-gio-0.22
Version:        0.22.6
Release:        %autorelease
Summary:        Rust crate "gio"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:e3848bcba3a35cc0a71df8ba8ecfd799d6bfb862342a53a4a915fb62213aa4e6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(futures-io-0.3/default) >= 0.3.0
Requires:       crate(futures-util-0.3) >= 0.3.0
Requires:       crate(gio-sys-0.22/default) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Requires:       crate(smallvec-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gio"

%package     -n %{name}+v2-58
Summary:        Rust bindings for the Gio library - feature "v2_58"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gio-sys-0.22/v2-58) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-58) >= 0.22.0
Provides:       crate(%{pkgname}/v2-58) = %{version}

%description -n %{name}+v2-58
This metapackage enables feature "v2_58" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-60
Summary:        Rust bindings for the Gio library - feature "v2_60"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-58) = %{version}
Requires:       crate(gio-sys-0.22/v2-60) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-60) >= 0.22.0
Provides:       crate(%{pkgname}/v2-60) = %{version}

%description -n %{name}+v2-60
This metapackage enables feature "v2_60" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-62
Summary:        Rust bindings for the Gio library - feature "v2_62"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-60) = %{version}
Requires:       crate(gio-sys-0.22/v2-62) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-62) >= 0.22.0
Provides:       crate(%{pkgname}/v2-62) = %{version}

%description -n %{name}+v2-62
This metapackage enables feature "v2_62" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-64
Summary:        Rust bindings for the Gio library - feature "v2_64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-62) = %{version}
Requires:       crate(gio-sys-0.22/v2-64) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-64) >= 0.22.0
Provides:       crate(%{pkgname}/v2-64) = %{version}

%description -n %{name}+v2-64
This metapackage enables feature "v2_64" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-66
Summary:        Rust bindings for the Gio library - feature "v2_66"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-64) = %{version}
Requires:       crate(gio-sys-0.22/v2-66) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-66) >= 0.22.0
Provides:       crate(%{pkgname}/v2-66) = %{version}

%description -n %{name}+v2-66
This metapackage enables feature "v2_66" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-68
Summary:        Rust bindings for the Gio library - feature "v2_68"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-66) = %{version}
Requires:       crate(gio-sys-0.22/v2-68) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-68) >= 0.22.0
Provides:       crate(%{pkgname}/v2-68) = %{version}

%description -n %{name}+v2-68
This metapackage enables feature "v2_68" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-70
Summary:        Rust bindings for the Gio library - feature "v2_70"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-68) = %{version}
Requires:       crate(gio-sys-0.22/v2-70) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-70) >= 0.22.0
Provides:       crate(%{pkgname}/v2-70) = %{version}

%description -n %{name}+v2-70
This metapackage enables feature "v2_70" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-72
Summary:        Rust bindings for the Gio library - feature "v2_72"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-70) = %{version}
Requires:       crate(gio-sys-0.22/v2-72) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-72) >= 0.22.0
Provides:       crate(%{pkgname}/v2-72) = %{version}

%description -n %{name}+v2-72
This metapackage enables feature "v2_72" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-74
Summary:        Rust bindings for the Gio library - feature "v2_74"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-72) = %{version}
Requires:       crate(gio-sys-0.22/v2-74) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-74) >= 0.22.0
Provides:       crate(%{pkgname}/v2-74) = %{version}

%description -n %{name}+v2-74
This metapackage enables feature "v2_74" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-76
Summary:        Rust bindings for the Gio library - feature "v2_76"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-74) = %{version}
Requires:       crate(gio-sys-0.22/v2-76) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-76) >= 0.22.0
Provides:       crate(%{pkgname}/v2-76) = %{version}

%description -n %{name}+v2-76
This metapackage enables feature "v2_76" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-78
Summary:        Rust bindings for the Gio library - feature "v2_78"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-76) = %{version}
Requires:       crate(gio-sys-0.22/v2-78) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-78) >= 0.22.0
Provides:       crate(%{pkgname}/v2-78) = %{version}

%description -n %{name}+v2-78
This metapackage enables feature "v2_78" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-80
Summary:        Rust bindings for the Gio library - feature "v2_80"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-78) = %{version}
Requires:       crate(gio-sys-0.22/v2-80) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-80) >= 0.22.0
Provides:       crate(%{pkgname}/v2-80) = %{version}

%description -n %{name}+v2-80
This metapackage enables feature "v2_80" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-82
Summary:        Rust bindings for the Gio library - feature "v2_82"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-80) = %{version}
Requires:       crate(gio-sys-0.22/v2-82) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-82) >= 0.22.0
Provides:       crate(%{pkgname}/v2-82) = %{version}

%description -n %{name}+v2-82
This metapackage enables feature "v2_82" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-84
Summary:        Rust bindings for the Gio library - feature "v2_84"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-82) = %{version}
Requires:       crate(gio-sys-0.22/v2-84) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-84) >= 0.22.0
Provides:       crate(%{pkgname}/v2-84) = %{version}

%description -n %{name}+v2-84
This metapackage enables feature "v2_84" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-86
Summary:        Rust bindings for the Gio library - feature "v2_86"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-84) = %{version}
Requires:       crate(gio-sys-0.22/v2-86) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-86) >= 0.22.0
Provides:       crate(%{pkgname}/v2-86) = %{version}

%description -n %{name}+v2-86
This metapackage enables feature "v2_86" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-88
Summary:        Rust bindings for the Gio library - feature "v2_88"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-86) = %{version}
Requires:       crate(gio-sys-0.22/v2-88) >= 0.22.0
Requires:       crate(glib-0.22/futures) >= 0.22.0
Requires:       crate(glib-0.22/v2-88) >= 0.22.0
Provides:       crate(%{pkgname}/v2-88) = %{version}

%description -n %{name}+v2-88
This metapackage enables feature "v2_88" for the Rust gio crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

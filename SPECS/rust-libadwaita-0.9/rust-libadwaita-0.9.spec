# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libadwaita
%global full_version 0.9.1
%global pkgname libadwaita-0.9

Name:           rust-libadwaita-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "libadwaita"
License:        MIT
URL:            https://world.pages.gitlab.gnome.org/Rust/libadwaita-rs/
#!RemoteAsset:  sha256:bc0da4e27b20d3e71f830e5b0f0188d22c257986bf421c02cfde777fe07932a4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gdk4-0.11/default) >= 0.11.0
Requires:       crate(gio-0.22/default) >= 0.22.0
Requires:       crate(glib-0.22/default) >= 0.22.0
Requires:       crate(gtk4-0.11/default) >= 0.11.0
Requires:       crate(libadwaita-sys-0.9/default) >= 0.9.1
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "libadwaita"

%package     -n %{name}+gio-v2-80
Summary:        Rust bindings for libadwaita - feature "gio_v2_80"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gio-0.22/v2-80) >= 0.22.0
Provides:       crate(%{pkgname}/gio-v2-80) = %{version}

%description -n %{name}+gio-v2-80
This metapackage enables feature "gio_v2_80" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gtk-v4-18
Summary:        Rust bindings for libadwaita - feature "gtk_v4_18"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gtk-v4-6) = %{version}
Requires:       crate(gtk4-0.11/v4-18) >= 0.11.0
Provides:       crate(%{pkgname}/gtk-v4-18) = %{version}

%description -n %{name}+gtk-v4-18
This metapackage enables feature "gtk_v4_18" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gtk-v4-2
Summary:        Rust bindings for libadwaita - feature "gtk_v4_2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gtk4-0.11/v4-2) >= 0.11.0
Provides:       crate(%{pkgname}/gtk-v4-2) = %{version}

%description -n %{name}+gtk-v4-2
This metapackage enables feature "gtk_v4_2" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gtk-v4-20
Summary:        Rust bindings for libadwaita - feature "gtk_v4_20"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gtk-v4-18) = %{version}
Requires:       crate(gtk4-0.11/v4-20) >= 0.11.0
Provides:       crate(%{pkgname}/gtk-v4-20) = %{version}

%description -n %{name}+gtk-v4-20
This metapackage enables feature "gtk_v4_20" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gtk-v4-22
Summary:        Rust bindings for libadwaita - feature "gtk_v4_22"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gtk-v4-20) = %{version}
Requires:       crate(gtk4-0.11/v4-22) >= 0.11.0
Provides:       crate(%{pkgname}/gtk-v4-22) = %{version}

%description -n %{name}+gtk-v4-22
This metapackage enables feature "gtk_v4_22" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gtk-v4-6
Summary:        Rust bindings for libadwaita - feature "gtk_v4_6"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gtk-v4-2) = %{version}
Requires:       crate(gtk4-0.11/v4-6) >= 0.11.0
Provides:       crate(%{pkgname}/gtk-v4-6) = %{version}

%description -n %{name}+gtk-v4-6
This metapackage enables feature "gtk_v4_6" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-1
Summary:        Rust bindings for libadwaita - feature "v1_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libadwaita-sys-0.9/v1-1) >= 0.9.1
Provides:       crate(%{pkgname}/v1-1) = %{version}

%description -n %{name}+v1-1
This metapackage enables feature "v1_1" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-2
Summary:        Rust bindings for libadwaita - feature "v1_2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-1) = %{version}
Requires:       crate(libadwaita-sys-0.9/v1-2) >= 0.9.1
Provides:       crate(%{pkgname}/v1-2) = %{version}

%description -n %{name}+v1-2
This metapackage enables feature "v1_2" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-3
Summary:        Rust bindings for libadwaita - feature "v1_3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-2) = %{version}
Requires:       crate(libadwaita-sys-0.9/v1-3) >= 0.9.1
Provides:       crate(%{pkgname}/v1-3) = %{version}

%description -n %{name}+v1-3
This metapackage enables feature "v1_3" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-4
Summary:        Rust bindings for libadwaita - feature "v1_4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-3) = %{version}
Requires:       crate(libadwaita-sys-0.9/v1-4) >= 0.9.1
Provides:       crate(%{pkgname}/v1-4) = %{version}

%description -n %{name}+v1-4
This metapackage enables feature "v1_4" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-5
Summary:        Rust bindings for libadwaita - feature "v1_5"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-4) = %{version}
Requires:       crate(libadwaita-sys-0.9/v1-5) >= 0.9.1
Provides:       crate(%{pkgname}/v1-5) = %{version}

%description -n %{name}+v1-5
This metapackage enables feature "v1_5" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-6
Summary:        Rust bindings for libadwaita - feature "v1_6"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-5) = %{version}
Requires:       crate(libadwaita-sys-0.9/v1-6) >= 0.9.1
Provides:       crate(%{pkgname}/v1-6) = %{version}

%description -n %{name}+v1-6
This metapackage enables feature "v1_6" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-7
Summary:        Rust bindings for libadwaita - feature "v1_7"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-6) = %{version}
Requires:       crate(libadwaita-sys-0.9/v1-7) >= 0.9.1
Provides:       crate(%{pkgname}/v1-7) = %{version}

%description -n %{name}+v1-7
This metapackage enables feature "v1_7" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-8
Summary:        Rust bindings for libadwaita - feature "v1_8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-7) = %{version}
Requires:       crate(libadwaita-sys-0.9/v1-8) >= 0.9.1
Provides:       crate(%{pkgname}/v1-8) = %{version}

%description -n %{name}+v1-8
This metapackage enables feature "v1_8" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-9
Summary:        Rust bindings for libadwaita - feature "v1_9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-8) = %{version}
Requires:       crate(libadwaita-sys-0.9/v1-9) >= 0.9.1
Provides:       crate(%{pkgname}/v1-9) = %{version}

%description -n %{name}+v1-9
This metapackage enables feature "v1_9" for the Rust libadwaita crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

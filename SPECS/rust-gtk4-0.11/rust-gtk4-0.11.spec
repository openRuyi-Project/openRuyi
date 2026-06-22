# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gtk4
%global full_version 0.11.3
%global pkgname gtk4-0.11

Name:           rust-gtk4-0.11
Version:        0.11.3
Release:        %autorelease
Summary:        Rust crate "gtk4"
License:        MIT
URL:            https://gtk-rs.org/gtk4-rs
#!RemoteAsset:  sha256:7181b837f04cbe93f79441475f7a00560a92cba7a72e38cc1a68b6f8b78eaae2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cairo-rs-0.22/default) >= 0.22.0
Requires:       crate(cairo-rs-0.22/use-glib) >= 0.22.0
Requires:       crate(field-offset-0.3/default) >= 0.3.0
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Requires:       crate(gdk-pixbuf-0.22/default) >= 0.22.0
Requires:       crate(gdk4-0.11/default) >= 0.11.0
Requires:       crate(gio-0.22/default) >= 0.22.0
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(glib-0.22/default) >= 0.22.0
Requires:       crate(glib-0.22/v2-66) >= 0.22.0
Requires:       crate(graphene-rs-0.22/default) >= 0.22.0
Requires:       crate(gsk4-0.11/default) >= 0.11.0
Requires:       crate(gtk4-macros-0.11/default) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/default) >= 0.11.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-0.22/default) >= 0.22.0
Requires:       crate(pango-0.22/v1-46) >= 0.22.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unsafe-assume-initialized) = %{version}

%description
Source code for takopackized Rust crate "gtk4"

%package     -n %{name}+blueprint
Summary:        Rust bindings of the GTK 4 library - feature "blueprint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gtk4-macros-0.11/blueprint) >= 0.11.0
Provides:       crate(%{pkgname}/blueprint) = %{version}

%description -n %{name}+blueprint
This metapackage enables feature "blueprint" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gio-v2-80
Summary:        Rust bindings of the GTK 4 library - feature "gio_v2_80"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(gio-0.22/v2-80) >= 0.22.0
Provides:       crate(%{pkgname}/gio-v2-80) = %{version}

%description -n %{name}+gio-v2-80
This metapackage enables feature "gio_v2_80" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnome-42
Summary:        Rust bindings of the GTK 4 library - feature "gnome_42"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-6) = %{version}
Requires:       crate(cairo-rs-0.22/use-glib) >= 0.22.0
Requires:       crate(cairo-rs-0.22/v1-16) >= 0.22.0
Requires:       crate(gdk-pixbuf-0.22/v2-42) >= 0.22.0
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(gio-0.22/v2-72) >= 0.22.0
Provides:       crate(%{pkgname}/gnome-42) = %{version}

%description -n %{name}+gnome-42
This metapackage enables feature "gnome_42" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnome-43
Summary:        Rust bindings of the GTK 4 library - feature "gnome_43"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-8) = %{version}
Requires:       crate(cairo-rs-0.22/use-glib) >= 0.22.0
Requires:       crate(cairo-rs-0.22/v1-16) >= 0.22.0
Requires:       crate(gdk-pixbuf-0.22/v2-42) >= 0.22.0
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(gio-0.22/v2-74) >= 0.22.0
Provides:       crate(%{pkgname}/gnome-43) = %{version}

%description -n %{name}+gnome-43
This metapackage enables feature "gnome_43" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnome-44
Summary:        Rust bindings of the GTK 4 library - feature "gnome_44"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-10) = %{version}
Requires:       crate(cairo-rs-0.22/use-glib) >= 0.22.0
Requires:       crate(cairo-rs-0.22/v1-16) >= 0.22.0
Requires:       crate(gdk-pixbuf-0.22/v2-42) >= 0.22.0
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(gio-0.22/v2-76) >= 0.22.0
Provides:       crate(%{pkgname}/gnome-44) = %{version}

%description -n %{name}+gnome-44
This metapackage enables feature "gnome_44" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnome-45
Summary:        Rust bindings of the GTK 4 library - feature "gnome_45"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-12) = %{version}
Requires:       crate(cairo-rs-0.22/use-glib) >= 0.22.0
Requires:       crate(cairo-rs-0.22/v1-16) >= 0.22.0
Requires:       crate(gdk-pixbuf-0.22/v2-42) >= 0.22.0
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(gio-0.22/v2-78) >= 0.22.0
Requires:       crate(pango-0.22/v1-46) >= 0.22.0
Requires:       crate(pango-0.22/v1-52) >= 0.22.0
Provides:       crate(%{pkgname}/gnome-45) = %{version}

%description -n %{name}+gnome-45
This metapackage enables feature "gnome_45" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnome-46
Summary:        Rust bindings of the GTK 4 library - feature "gnome_46"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gio-v2-80) = %{version}
Requires:       crate(%{pkgname}/v4-14) = %{version}
Requires:       crate(cairo-rs-0.22/use-glib) >= 0.22.0
Requires:       crate(cairo-rs-0.22/v1-16) >= 0.22.0
Requires:       crate(gdk-pixbuf-0.22/v2-42) >= 0.22.0
Requires:       crate(pango-0.22/v1-46) >= 0.22.0
Requires:       crate(pango-0.22/v1-52) >= 0.22.0
Provides:       crate(%{pkgname}/gnome-46) = %{version}

%description -n %{name}+gnome-46
This metapackage enables feature "gnome_46" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnome-47
Summary:        Rust bindings of the GTK 4 library - feature "gnome_47"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnome-46) = %{version}
Requires:       crate(%{pkgname}/v4-16) = %{version}
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(gio-0.22/v2-82) >= 0.22.0
Provides:       crate(%{pkgname}/gnome-47) = %{version}

%description -n %{name}+gnome-47
This metapackage enables feature "gnome_47" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnome-48
Summary:        Rust bindings of the GTK 4 library - feature "gnome_48"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnome-47) = %{version}
Requires:       crate(%{pkgname}/v4-18) = %{version}
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(gio-0.22/v2-84) >= 0.22.0
Provides:       crate(%{pkgname}/gnome-48) = %{version}

%description -n %{name}+gnome-48
This metapackage enables feature "gnome_48" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnome-49
Summary:        Rust bindings of the GTK 4 library - feature "gnome_49"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnome-48) = %{version}
Requires:       crate(%{pkgname}/v4-20) = %{version}
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(gio-0.22/v2-86) >= 0.22.0
Provides:       crate(%{pkgname}/gnome-49) = %{version}

%description -n %{name}+gnome-49
This metapackage enables feature "gnome_49" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnome-50
Summary:        Rust bindings of the GTK 4 library - feature "gnome_50"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnome-49) = %{version}
Requires:       crate(%{pkgname}/v4-22) = %{version}
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(gio-0.22/v2-88) >= 0.22.0
Provides:       crate(%{pkgname}/gnome-50) = %{version}

%description -n %{name}+gnome-50
This metapackage enables feature "gnome_50" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-10
Summary:        Rust bindings of the GTK 4 library - feature "v4_10"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-8) = %{version}
Requires:       crate(gdk4-0.11/v4-10) >= 0.11.0
Requires:       crate(gsk4-0.11/v4-10) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-10) >= 0.11.0
Provides:       crate(%{pkgname}/v4-10) = %{version}

%description -n %{name}+v4-10
This metapackage enables feature "v4_10" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-12
Summary:        Rust bindings of the GTK 4 library - feature "v4_12"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-10) = %{version}
Requires:       crate(gdk4-0.11/v4-12) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-12) >= 0.11.0
Provides:       crate(%{pkgname}/v4-12) = %{version}

%description -n %{name}+v4-12
This metapackage enables feature "v4_12" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-14
Summary:        Rust bindings of the GTK 4 library - feature "v4_14"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-12) = %{version}
Requires:       crate(gdk4-0.11/v4-14) >= 0.11.0
Requires:       crate(gsk4-0.11/v4-14) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-14) >= 0.11.0
Provides:       crate(%{pkgname}/v4-14) = %{version}

%description -n %{name}+v4-14
This metapackage enables feature "v4_14" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-16
Summary:        Rust bindings of the GTK 4 library - feature "v4_16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-14) = %{version}
Requires:       crate(gdk4-0.11/v4-16) >= 0.11.0
Requires:       crate(gsk4-0.11/v4-16) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-16) >= 0.11.0
Provides:       crate(%{pkgname}/v4-16) = %{version}

%description -n %{name}+v4-16
This metapackage enables feature "v4_16" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-18
Summary:        Rust bindings of the GTK 4 library - feature "v4_18"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-16) = %{version}
Requires:       crate(gdk4-0.11/v4-18) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-18) >= 0.11.0
Provides:       crate(%{pkgname}/v4-18) = %{version}

%description -n %{name}+v4-18
This metapackage enables feature "v4_18" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-2
Summary:        Rust bindings of the GTK 4 library - feature "v4_2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gdk4-0.11/v4-2) >= 0.11.0
Requires:       crate(gsk4-0.11/v4-2) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-2) >= 0.11.0
Provides:       crate(%{pkgname}/v4-2) = %{version}

%description -n %{name}+v4-2
This metapackage enables feature "v4_2" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-20
Summary:        Rust bindings of the GTK 4 library - feature "v4_20"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-18) = %{version}
Requires:       crate(gdk4-0.11/v4-20) >= 0.11.0
Requires:       crate(gsk4-0.11/v4-20) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-20) >= 0.11.0
Provides:       crate(%{pkgname}/v4-20) = %{version}

%description -n %{name}+v4-20
This metapackage enables feature "v4_20" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-22
Summary:        Rust bindings of the GTK 4 library - feature "v4_22"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-20) = %{version}
Requires:       crate(gdk4-0.11/v4-22) >= 0.11.0
Requires:       crate(gsk4-0.11/v4-22) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-22) >= 0.11.0
Provides:       crate(%{pkgname}/v4-22) = %{version}

%description -n %{name}+v4-22
This metapackage enables feature "v4_22" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-24
Summary:        Rust bindings of the GTK 4 library - feature "v4_24"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-22) = %{version}
Requires:       crate(gdk4-0.11/v4-24) >= 0.11.0
Requires:       crate(gsk4-0.11/v4-22) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-24) >= 0.11.0
Provides:       crate(%{pkgname}/v4-24) = %{version}

%description -n %{name}+v4-24
This metapackage enables feature "v4_24" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-4
Summary:        Rust bindings of the GTK 4 library - feature "v4_4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-2) = %{version}
Requires:       crate(gdk4-0.11/v4-4) >= 0.11.0
Requires:       crate(gsk4-0.11/v4-4) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-4) >= 0.11.0
Provides:       crate(%{pkgname}/v4-4) = %{version}

%description -n %{name}+v4-4
This metapackage enables feature "v4_4" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-6
Summary:        Rust bindings of the GTK 4 library - feature "v4_6"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-4) = %{version}
Requires:       crate(gdk4-0.11/v4-6) >= 0.11.0
Requires:       crate(gsk4-0.11/v4-6) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-6) >= 0.11.0
Requires:       crate(pango-0.22/v1-46) >= 0.22.0
Requires:       crate(pango-0.22/v1-50) >= 0.22.0
Provides:       crate(%{pkgname}/v4-6) = %{version}

%description -n %{name}+v4-6
This metapackage enables feature "v4_6" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-8
Summary:        Rust bindings of the GTK 4 library - feature "v4_8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-6) = %{version}
Requires:       crate(gdk4-0.11/v4-8) >= 0.11.0
Requires:       crate(gtk4-sys-0.11/v4-8) >= 0.11.0
Provides:       crate(%{pkgname}/v4-8) = %{version}

%description -n %{name}+v4-8
This metapackage enables feature "v4_8" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xml-validation
Summary:        Rust bindings of the GTK 4 library - feature "xml_validation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gtk4-macros-0.11/xml-validation) >= 0.11.0
Provides:       crate(%{pkgname}/xml-validation) = %{version}

%description -n %{name}+xml-validation
This metapackage enables feature "xml_validation" for the Rust gtk4 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

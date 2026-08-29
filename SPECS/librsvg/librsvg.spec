# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global cairo_version 1.18.0

Name:           librsvg
Version:        2.62.3
Release:        %autorelease
Summary:        An SVG library based on cairo
License:        LGPL-2.1-or-later
URL:            https://github.com/GNOME/librsvg
#!RemoteAsset:  sha256:7eb449b2722a768021356f66dfee3202c229b54ed4e6a70ce40c090e97ff16f2
Source0:        https://download.gnome.org/sources/librsvg/2.62/librsvg-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Ddocs=disabled
BuildOption(conf):  -Dtests=false
BuildOption(conf):  -Dpixbuf-loader=disabled
BuildOption(conf):  -Ddocs=enabled
BuildOption(conf):  -Dtests=true

BuildRequires:  python3dist(docutils)
BuildRequires:  crate(assert-cmd-2/default) >= 2.2.2
BuildRequires:  crate(bitflags-2/default) >= 2.13.0
BuildRequires:  crate(cairo-rs-0.22/default) >= 0.22.0
BuildRequires:  crate(cairo-rs-0.22/pdf) >= 0.22.0
BuildRequires:  crate(cairo-rs-0.22/png) >= 0.22.0
BuildRequires:  crate(cairo-rs-0.22/ps) >= 0.22.0
BuildRequires:  crate(cairo-rs-0.22/svg) >= 0.22.0
BuildRequires:  crate(cairo-rs-0.22/v1-16) >= 0.22.0
BuildRequires:  crate(cairo-rs-0.22/v1-18) >= 0.22.0
BuildRequires:  crate(cairo-sys-rs-0.22/default) >= 0.22.0
BuildRequires:  crate(cast-0.3/default) >= 0.3.0
BuildRequires:  crate(chrono-0.4/clock) >= 0.4.44
BuildRequires:  crate(chrono-0.4/std) >= 0.4.44
BuildRequires:  crate(clap-4/cargo) >= 4.6.1
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/derive) >= 4.6.1
BuildRequires:  crate(clap-complete-4/default) >= 4.6.3
BuildRequires:  crate(criterion-0.7/default) >= 0.7.0
BuildRequires:  crate(cssparser-0.35/default) >= 0.35.0
BuildRequires:  crate(cssparser-color-0.3/default) >= 0.3.0
BuildRequires:  crate(data-url-0.3/default) >= 0.3.2
BuildRequires:  crate(encoding-rs-0.8/default) >= 0.8.35
BuildRequires:  crate(float-cmp-0.10/default) >= 0.10.0
BuildRequires:  crate(gdk-pixbuf-0.22/default) >= 0.22.0
BuildRequires:  crate(gdk-pixbuf-sys-0.22/default) >= 0.22.0
BuildRequires:  crate(gio-0.22/default) >= 0.22.6
BuildRequires:  crate(gio-sys-0.22/default) >= 0.22.0
BuildRequires:  crate(gio-unix-0.22/default) >= 0.22.6
BuildRequires:  crate(gio-win32-0.22/default) >= 0.22.6
BuildRequires:  crate(glib-0.22/default) >= 0.22.7
BuildRequires:  crate(glib-sys-0.22/default) >= 0.22.6
BuildRequires:  crate(gobject-sys-0.22/default) >= 0.22.6
BuildRequires:  crate(image-0.25/gif) >= 0.25.10
BuildRequires:  crate(image-0.25/jpeg) >= 0.25.10
BuildRequires:  crate(image-0.25/png) >= 0.25.10
BuildRequires:  crate(image-0.25/webp) >= 0.25.10
BuildRequires:  crate(image-0.25/avif-native) >= 0.25.10
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(language-tags-0.3/default) >= 0.3.2
BuildRequires:  crate(libc-0.2/default) >= 0.2.186
BuildRequires:  crate(locale-config-0.3/default) >= 0.3.0
BuildRequires:  crate(lopdf-0.38/default) >= 0.38.0
BuildRequires:  crate(markup5ever-0.35/default) >= 0.35.0
BuildRequires:  crate(matches-0.1/default) >= 0.1.10
BuildRequires:  crate(mutants-0.0.3/default) >= 0.0.3
BuildRequires:  crate(nalgebra-0.34/default) >= 0.34.2
BuildRequires:  crate(num-traits-0.2/default) >= 0.2.19
BuildRequires:  crate(pango-0.22/default) >= 0.22.6
BuildRequires:  crate(pango-0.22/v1-46) >= 0.22.6
BuildRequires:  crate(pangocairo-0.22/default) >= 0.22.0
BuildRequires:  crate(png-0.18/default) >= 0.18.1
BuildRequires:  crate(precomputed-hash-0.1/default) >= 0.1.1
BuildRequires:  crate(predicates-3/default) >= 3.1.4
BuildRequires:  crate(pretty-assertions-1/default) >= 1.4.1
BuildRequires:  crate(proptest-1/default) >= 1.11.0
BuildRequires:  crate(quick-error-2/default) >= 2.0.1
BuildRequires:  crate(rayon-1/default) >= 1.12.0
BuildRequires:  crate(rctree-0.6/default) >= 0.6.0
BuildRequires:  crate(regex-1/default) >= 1.12.3
BuildRequires:  crate(rgb-0.8/argb) >= 0.8.53
BuildRequires:  crate(rgb-0.8/default) >= 0.8.53
BuildRequires:  crate(selectors-0.31/default) >= 0.31.0
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.150
BuildRequires:  crate(shell-words-1/default) >= 1.1.1
BuildRequires:  crate(string-cache-0.9/default) >= 0.9.0
BuildRequires:  crate(system-deps-7/default) >= 7.0.8
BuildRequires:  crate(tempfile-3/default) >= 3.27.0
BuildRequires:  crate(tinyvec-1/alloc) >= 1.11.0
BuildRequires:  crate(tinyvec-1/default) >= 1.11.0
BuildRequires:  crate(tinyvec-1/rustc-1-55) >= 1.11.0
BuildRequires:  crate(url-2/default) >= 2.5.8
BuildRequires:  crate(xml5ever-0.35/default) >= 0.35.0
BuildRequires:  crate(yeslogic-fontconfig-sys-6/default) >= 6.0.1
BuildRequires:  meson >= 1.2.0
BuildRequires:  gcc
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  cargo-c
BuildRequires:  python3dist(docutils)
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(cairo) >= %{cairo_version}
BuildRequires:  pkgconfig(cairo-gobject) >= %{cairo_version}
BuildRequires:  pkgconfig(cairo-png) >= %{cairo_version}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  vala
BuildRequires:  pkgconfig(gi-docgen)

Requires:       cairo%{?_isa} >= %{cairo_version}
Requires:       cairo-gobject%{?_isa} >= %{cairo_version}

%description
An SVG library based on cairo.

%package        devel
Summary:        Libraries and include files for developing with librsvg
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for librsvg.

%prep -a
%rust_setup_registry

sed -i 's/, "--locked"//g' meson/cargo_wrapper.py

%build -p
rm -rf Cargo.lock

%install -a
rm -f %{buildroot}%{_docdir}/librsvg*/COMPILING.md

%files
%doc NEWS README.md
%license COPYING.LIB
%{_libdir}/librsvg-2.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Rsvg-2.0.typelib
%{_bindir}/rsvg-convert
%{_mandir}/man1/rsvg-convert.1*

%files devel
%{_libdir}/librsvg-2.so
%{_includedir}/librsvg-2.0/
%{_libdir}/pkgconfig/librsvg-2.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Rsvg-2.0.gir
%{_datadir}/vala/vapi/librsvg-2.0.vapi
%{_datadir}/vala/vapi/librsvg-2.0.deps
%{_docdir}/Rsvg-2.0

%changelog
%autochangelog

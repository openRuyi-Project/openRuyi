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
BuildRequires:  crate(adler2-2) >= 2.0.1
BuildRequires:  crate(ahash-0.8) >= 0.8.12
BuildRequires:  crate(anstream-1) >= 1.0.0
BuildRequires:  crate(anstyle-query-1) >= 1.1.5
BuildRequires:  crate(anstyle-wincon-3) >= 3.0.11
BuildRequires:  crate(approx-0.5) >= 0.5.1
BuildRequires:  crate(autocfg-1) >= 1.5.0
BuildRequires:  crate(cc-1) >= 1.2.63
BuildRequires:  crate(chrono-0.4) >= 0.4.44
BuildRequires:  crate(clap-complete-4) >= 4.6.3
BuildRequires:  crate(clap-derive-4) >= 4.6.1
BuildRequires:  crate(color-quant-1) >= 1.1.0
BuildRequires:  crate(cssparser-color-0.3) >= 0.3.0
BuildRequires:  crate(data-url-0.3) >= 0.3.2
BuildRequires:  crate(dav1d-0.11) >= 0.11.1
BuildRequires:  crate(displaydoc-0.2) >= 0.2.5
BuildRequires:  crate(equivalent-1) >= 1.0.2
BuildRequires:  crate(float-cmp-0.10) >= 0.10.0
BuildRequires:  crate(gdk-pixbuf-0.22) >= 0.22.0
BuildRequires:  crate(gif-0.14) >= 0.14.2
BuildRequires:  crate(gio-unix-0.22) >= 0.22.6
BuildRequires:  crate(gio-win32-0.22) >= 0.22.6
BuildRequires:  crate(glam-0.14) >= 0.14.0
BuildRequires:  crate(glam-0.15) >= 0.15.2
BuildRequires:  crate(glam-0.16) >= 0.16.0
BuildRequires:  crate(glam-0.17) >= 0.17.3
BuildRequires:  crate(glam-0.18) >= 0.18.0
BuildRequires:  crate(glam-0.19) >= 0.19.0
BuildRequires:  crate(glam-0.20) >= 0.20.5
BuildRequires:  crate(glam-0.21) >= 0.21.3
BuildRequires:  crate(glam-0.22) >= 0.22.0
BuildRequires:  crate(glam-0.23) >= 0.23.0
BuildRequires:  crate(glam-0.24) >= 0.24.2
BuildRequires:  crate(glam-0.25) >= 0.25.0
BuildRequires:  crate(glam-0.27) >= 0.27.0
BuildRequires:  crate(glam-0.28) >= 0.28.0
BuildRequires:  crate(glam-0.29) >= 0.29.3
BuildRequires:  crate(glam-0.30) >= 0.30.10
BuildRequires:  crate(glam-0.31) >= 0.31.1
BuildRequires:  crate(glam-0.32) >= 0.32.1
BuildRequires:  crate(glib-macros-0.22) >= 0.22.6
BuildRequires:  crate(iana-time-zone-0.1) >= 0.1.65
BuildRequires:  crate(image-0.25) >= 0.25.10
BuildRequires:  crate(image-webp-0.2) >= 0.2.4
BuildRequires:  crate(itertools-0.14) >= 0.14.0
BuildRequires:  crate(language-tags-0.3) >= 0.3.2
BuildRequires:  crate(litemap-0.8) >= 0.8.2
BuildRequires:  crate(locale-config-0.3) >= 0.3.0
BuildRequires:  crate(matrixmultiply-0.3) >= 0.3.10
BuildRequires:  crate(mp4parse-0.17) >= 0.17.0
BuildRequires:  crate(mutants-0.0.3) >= 0.0.3
BuildRequires:  crate(nalgebra-0.34) >= 0.34.2
BuildRequires:  crate(nalgebra-macros-0.3) >= 0.3.0
BuildRequires:  crate(num-complex-0.4) >= 0.4.6
BuildRequires:  crate(pangocairo-0.22) >= 0.22.0
BuildRequires:  crate(phf-codegen-0.11) >= 0.11.3
BuildRequires:  crate(png-0.18) >= 0.18.1
BuildRequires:  crate(rayon-1) >= 1.12.0
BuildRequires:  crate(rctree-0.6) >= 0.6.0
BuildRequires:  crate(rgb-0.8) >= 0.8.53
BuildRequires:  crate(rustc-version-0.4) >= 0.4.1
BuildRequires:  crate(rustversion-1) >= 1.0.22
BuildRequires:  crate(scopeguard-1) >= 1.2.0
BuildRequires:  crate(selectors-0.31) >= 0.31.0
BuildRequires:  crate(simba-0.9) >= 0.9.1
BuildRequires:  crate(string-cache-0.9) >= 0.9.0
BuildRequires:  crate(strsim-0.11) >= 0.11.1
BuildRequires:  crate(system-deps-7) >= 7.0.8
BuildRequires:  crate(url-2) >= 2.5.8
BuildRequires:  crate(version-check-0.9) >= 0.9.5
BuildRequires:  crate(wide-0.7) >= 0.7.33
BuildRequires:  crate(windows-core-0.62) >= 0.62.2
BuildRequires:  crate(windows-sys-0.61) >= 0.61.2
BuildRequires:  crate(winnow-1) >= 1.0.3
BuildRequires:  crate(writeable-0.6) >= 0.6.2
BuildRequires:  crate(xml5ever-0.35) >= 0.35.0
BuildRequires:  crate(yeslogic-fontconfig-sys-6) >= 6.0.1
BuildRequires:  crate(zerofrom-derive-0.1) >= 0.1.7
BuildRequires:  crate(zune-jpeg-0.5) >= 0.5.15
BuildRequires:  crate(assert-cmd-2) >= 2.2.2
BuildRequires:  crate(bit-set-0.5) >= 0.5.3
BuildRequires:  crate(bit-vec-0.6) >= 0.6.3
BuildRequires:  crate(criterion-0.7) >= 0.7.0
BuildRequires:  crate(foldhash-0.1) >= 0.1.5
BuildRequires:  crate(getrandom-0.2) >= 0.2.17
BuildRequires:  crate(getrandom-0.4) >= 0.4.2
BuildRequires:  crate(half-2) >= 2.7.1
BuildRequires:  crate(jiff-0.2) >= 0.2.24
BuildRequires:  crate(jiff-tzdb-platform-0.1) >= 0.1.3
BuildRequires:  crate(lopdf-0.38) >= 0.38.0
BuildRequires:  crate(matches-0.1) >= 0.1.10
BuildRequires:  crate(normalize-line-endings-0.3) >= 0.3.0
BuildRequires:  crate(plotters-0.3) >= 0.3.7
BuildRequires:  crate(plotters-svg-0.3) >= 0.3.7
BuildRequires:  crate(portable-atomic-util-0.2) >= 0.2.7
BuildRequires:  crate(pretty-assertions-1) >= 1.4.1
BuildRequires:  crate(proptest-1) >= 1.0.0
BuildRequires:  crate(rand-chacha-0.3) >= 0.3.1
BuildRequires:  crate(r-efi-5) >= 5.3.0
BuildRequires:  crate(regex-syntax-0.6) >= 0.6.0
BuildRequires:  crate(rusty-fork-0.3) >= 0.3.0
BuildRequires:  crate(shell-words-1) >= 1.1.1
BuildRequires:  crate(time-0.3) >= 0.3.47
BuildRequires:  crate(time-macros-0.2) >= 0.2.27
BuildRequires:  crate(wasi-0.11) >= 0.11.1
BuildRequires:  crate(wasip2-1) >= 1.0.3
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

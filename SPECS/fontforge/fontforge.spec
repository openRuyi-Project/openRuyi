# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Change these to 1 once we have them
%bcond gui 0
%bcond doc 0

Name:           fontforge
Version:        20251009
Release:        %autorelease
Summary:        Outline and bitmap font editor
License:        GPL-3.0-or-later
URL:            https://fontforge.org/
VCS:            git:https://github.com/fontforge/fontforge
#!RemoteAsset
Source0:        https://github.com/fontforge/fontforge/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_BUILD_TYPE=Release
BuildOption(conf):  -DENABLE_WOFF2=ON
%if %{without gui}
BuildOption(conf):  -DENABLE_GUI=OFF
%endif
%if %{without doc}
BuildOption(conf):  -DENABLE_DOCS=OFF
%endif
BuildOption(conf):  -DPYHOOK_INSTALL_DIR=%{python3_sitearch}
BuildOption(conf):  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}/html

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  giflib-devel
BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libspiro)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(libwoff2common)
%if %{with gui}
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
%endif
%if %{with doc}
BuildRequires:  python3-sphinx
%endif

%description
FontForge (former PfaEdit) is a font editor for outline and bitmap
fonts. It supports a range of font formats, including PostScript
(ASCII and binary Type 1, some Type 3 and Type 0), TrueType, OpenType
(Type2) and CID-keyed fonts.

%package        devel
Summary:        Development files for fontforge
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with doc}
Requires:       %{name}-doc = %{version}-%{release}
%endif

%description    devel
This package includes the library files you will need to compile
applications against fontforge.

%if %{with doc}
%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
This package contains documentation files for %{name}.
%endif

%install -a
# remove unneeded .a files
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

rm -f %{buildroot}%{_datadir}/doc/fontforge/{.buildinfo,.nojekyll}

%find_lang FontForge --generate-subpackages

%files -f FontForge.lang
%doc AUTHORS
%license LICENSE COPYING.gplv3
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_datadir}/fontforge
%if %{with gui}
%{_datadir}/applications/*FontForge.desktop
%{_datadir}/mime/packages/fontforge.xml
%{_datadir}/icons/hicolor/*/apps/org.fontforge.FontForge*
%endif
%{_mandir}/man1/*.1*
%{python3_sitearch}/fontforge.so
%{python3_sitearch}/psMat.so

%files devel
%{_libdir}/lib*.so

%if %{with doc}
%files doc
%doc %{_docdir}/%{name}/html
%endif

%changelog
%autochangelog

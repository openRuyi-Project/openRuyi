# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xorgproto
Version:        2024.1
Release:        %autorelease
Summary:        X.Org X11 Protocol headers
License:        BSD-2-Clause AND HPND AND HPND-sell-variant AND ICU AND MIT AND MIT-open-group AND SGI-B-2.0 AND SMLNJ AND X11 AND X11-distribute-modifications-variant
URL:            https://www.x.org
VCS:            git:https://gitlab.freedesktop.org/xorg/proto/xorgproto.git
#!RemoteAsset
Source0:        https://www.x.org/pub/individual/proto/xorgproto-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    meson

BuildRequires:  pkgconfig
BuildRequires:  meson

%description
X.Org X11 Protocol headers

%install -a
# remove unused headers and pkgconfig files
for i in apple windows trap; do
    rm -f %{buildroot}%{_includedir}/X11/extensions/*${i}*
    rm -f %{buildroot}%{_datadir}/pkgconfig/*${i}*
done

# remove html/svg docs if generated
rm -f %{buildroot}%{_docdir}/*/*.{html,svg}

%files
%doc COPYING-*
%doc *.txt
%dir %{_includedir}/GL
%{_includedir}/GL/glxint.h
%{_includedir}/GL/glxmd.h
%{_includedir}/GL/glxproto.h
%{_includedir}/GL/glxtokens.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/glcore.h
%dir %{_includedir}/X11
%{_includedir}/X11/DECkeysym.h
%{_includedir}/X11/HPkeysym.h
%{_includedir}/X11/Sunkeysym.h
%{_includedir}/X11/X.h
%{_includedir}/X11/XF86keysym.h
%{_includedir}/X11/XWDFile.h
%{_includedir}/X11/Xalloca.h
%{_includedir}/X11/Xarch.h
%{_includedir}/X11/Xatom.h
%{_includedir}/X11/Xdefs.h
%{_includedir}/X11/Xfuncproto.h
%{_includedir}/X11/Xfuncs.h
%{_includedir}/X11/Xmd.h
%{_includedir}/X11/Xos.h
%{_includedir}/X11/Xos_r.h
%{_includedir}/X11/Xosdefs.h
%{_includedir}/X11/Xpoll.h
%{_includedir}/X11/Xproto.h
%{_includedir}/X11/Xprotostr.h
%{_includedir}/X11/Xthreads.h
%{_includedir}/X11/Xw32defs.h
%{_includedir}/X11/Xwindows.h
%{_includedir}/X11/Xwinsock.h
%{_includedir}/X11/ap_keysym.h
%dir %{_includedir}/X11/dri
%{_includedir}/X11/dri/xf86dri.h
%{_includedir}/X11/dri/xf86driproto.h
%{_includedir}/X11/dri/xf86dristr.h
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/*
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/*
%{_includedir}/X11/keysym.h
%{_includedir}/X11/keysymdef.h
%{_datadir}/pkgconfig/*.pc
%{_docdir}/xorgproto/*
%dir %{_docdir}/xorgproto/

%changelog
%autochangelog

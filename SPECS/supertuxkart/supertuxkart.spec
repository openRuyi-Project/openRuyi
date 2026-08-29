# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           supertuxkart
Version:        1.5
Release:        %autorelease
Summary:        A 3D open-source arcade racer with a variety of characters, tracks and modes to play
License:        CC-BY-SA-3.0 AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://supertuxkart.net/
VCS:            git:https://github.com/supertuxkart/stk-code
#!RemoteAsset:  sha256:33cf8841e4ff4082d80b9248014295bbbea61d14683e86dff100e3ab8f7b27cb
Source:         https://github.com/supertuxkart/stk-code/releases/download/%{version}/SuperTuxKart-%{version}-src.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_RECORDER=OFF
BuildOption(conf):  -DUSE_SYSTEM_ANGELSCRIPT=ON
BuildOption(conf):  -DUSE_SYSTEM_WIIUSE=ON
BuildOption(conf):  -DOpenGL_GL_PREFERENCE=GLVND
BuildOption(conf):  -DUSE_SYSTEM_SQUISH=ON
BuildOption(conf):  -DSQUISH_LIBRARY=%{_libdir}/libsquish.so
BuildOption(conf):  -DSQUISH_INCLUDEDIR=${PWD}/stk-squish-compat

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wiiuse)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(raqm)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  cmake(libsquish)
BuildRequires:  cmake(Angelscript)
%ifnarch x86_64
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
%endif

Requires:       hicolor-icon-theme
Requires:       supertuxkart-data = %{version}

%description
SuperTuxKart is a 3D open-source arcade racer with a variety of characters, tracks, and modes to play.

%package        data
Summary:        Data files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    data
Data files for SuperTuxKart a Free 3d kart racing game.

%prep -a
# supertuxkart expects <squish.h>, while this libsquish installs headers under /usr/include/squish/squish/.
mkdir -p stk-squish-compat/squish
ln -s %{_includedir}/squish/squish/squish.h stk-squish-compat/squish.h
ln -s %{_includedir}/squish/squish/squish_export.h stk-squish-compat/squish/squish_export.h

%files
%doc CHANGELOG.md README.md
%license COPYING
%{_bindir}/supertuxkart
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/net.supertuxkart.SuperTuxKart.metainfo.xml
%{_datadir}/applications/supertuxkart.desktop
%{_datadir}/icons/hicolor/

%files data
%{_datadir}/supertuxkart/

%changelog
%autochangelog

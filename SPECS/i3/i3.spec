# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Docs and man pages ship pre-generated in the release tarball and are installed
# by default; enable this to regenerate them from source (needs asciidoc/xmlto).
%bcond docs 0

Name:           i3
Version:        4.25.1
Release:        %autorelease
Summary:        Improved tiling window manager
License:        BSD-3-Clause
URL:            https://i3wm.org
VCS:            git:https://github.com/i3/i3.git
#!RemoteAsset:  sha256:4a742bbe81b9e5ee6057f42a8e3c691d88894e93f1a5d81fe239128512ac05c0
Source0:        https://i3wm.org/downloads/%{name}-%{version}.tar.xz
BuildSystem:    meson

%if %{with docs}
BuildOption(conf):  -Ddocs=true
BuildOption(conf):  -Dmans=true
%else
BuildOption(conf):  -Ddocs=false
BuildOption(conf):  -Dmans=false
%endif

BuildRequires:  bash
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  libev-devel >= 4.0
BuildRequires:  meson >= 0.53
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(TAP::Harness)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(X11::XCB) >= 0.12
BuildRequires:  perl(common::sense)
BuildRequires:  pkgconfig(cairo) >= 1.14.4
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libpcre2-8) >= 10
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xcb) >= 1.1.93
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.0
BuildRequires:  pkgconfig(xkbcommon-x11) >= 0.4.0
BuildRequires:  pkgconfig(yajl) >= 2.0.1
BuildRequires:  xorg-server-xephyr
BuildRequires:  xorg-server-xvfb
# Only needed when regenerating docs/man pages from source (see %%bcond docs).
%if %{with docs}
BuildRequires:  asciidoc
BuildRequires:  xmlto
%endif

Requires:       perl
Requires:       perl(AnyEvent::I3) >= 0.19
Requires:       perl(JSON::XS)
Requires:       xkeyboard-config

# Applications referenced by the upstream default configuration, when packaged:
# Recommends:     dmenu
# Recommends:     i3lock
# Recommends:     i3status

%description
i3 is a tiling window manager for X11. It uses xcb for asynchronous
communication with X11 and focuses on predictable, documented behavior.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files for applications that use the i3 IPC interface.

%prep -a
# These scripts are installed into %%{_bindir}; use the system Perl path.
find . -maxdepth 1 -type f -name 'i3*' -exec sed -i -e '1s;^#!/usr/bin/env perl;#!/usr/bin/perl;' {} +
# Keep the upstream tests complete, but run them serially in OBS to avoid
# spawning excessive nested X servers on build workers.
sed -i -e 's/my $parallel = undef;/my $parallel = 1;/' testcases/complete-run.pl.in

%check
mkdir -p /tmp/.X11-unix
chmod 1777 /tmp/.X11-unix || :
mkdir -p i3-test-bin
cat > i3-test-bin/xvfb-run <<'EOF'
#!/bin/sh
if [ "$1" = "--help" ]; then
    exit 0
fi
exec "$@"
EOF
chmod +x i3-test-bin/xvfb-run
PATH="$PWD/i3-test-bin:$PATH" %meson_test --timeout-multiplier 10 --print-errorlogs || {
    cat %{_vpath_builddir}/latest/complete-run.log || true
    find %{_vpath_builddir}/latest -maxdepth 1 -type f -name 'output-for-*' -print -exec cat {} \; || true
    exit 1
}
desktop-file-validate %{buildroot}%{_datadir}/applications/i3.desktop

%files
%doc RELEASE-NOTES-%{version}
%license LICENSE
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/config.keycodes
%{_bindir}/%{name}*
%{_docdir}/%{name}/*.css
%{_docdir}/%{name}/*.html
%{_docdir}/%{name}/*.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/xsessions/%{name}-with-shmlog.desktop
%{_mandir}/man1/%{name}*.1*

%files devel
%license LICENSE
%{_includedir}/%{name}/ipc.h

%changelog
%autochangelog

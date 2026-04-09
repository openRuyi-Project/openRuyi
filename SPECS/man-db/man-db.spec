# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           man-db
Version:        2.13.1
Release:        %autorelease
Summary:        Tools for searching and reading man pages
License:        GPL-2.0-or-later
URL:            https://savannah.nongnu.org/projects/man-db
VCS:            git:https://git.savannah.nongnu.org/git/man-db.git
#!RemoteAsset
Source0:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz.asc
BuildSystem:    autotools

BuildOption(conf):  --with-sections="1 1p 8 2 3 3p 3pm 4 5 6 7 9 0p n l p o 1x 2x 3x 4x 5x 6x 7x 8x"
BuildOption(conf):  --disable-setuid
BuildOption(conf):  --enable-cache-owner=root
BuildOption(conf):  --with-systemdsystemunitdir=/usr/lib/systemd/system
BuildOption(conf):  --with-override-dir=overrides

BuildRequires:  make
BuildRequires:  less
BuildRequires:  groff
BuildRequires:  groff-base
BuildRequires:  gdbm-devel
BuildRequires:  pkgconfig(libpipeline)
BuildRequires:  pkgconfig(zlib)

Provides:       man = %{version}-%{release}
Provides:       man-pages-reader = %{version}-%{release}

Requires:       groff
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives

%description
The man-db package includes five tools for browsing man-pages:
man, whatis, apropos, manpath and lexgrog. man formats and displays
manual pages. whatis searches the manual page names. apropos searches the
manual page names and descriptions. manpath determines search path
for manual pages. lexgrog directly reads header information in
manual pages.

%install -a
# rename files for alternative usage
for f in man apropos whatis; do
   mv %{buildroot}%{_bindir}/$f %{buildroot}%{_bindir}/$f.%{name}
   touch %{buildroot}%{_bindir}/$f
   mv %{buildroot}%{_mandir}/man1/$f.1 %{buildroot}%{_mandir}/man1/$f.%{name}.1
   touch %{buildroot}%{_mandir}/man1/$f.1
done

# move the documentation to the relevant place
mv %{buildroot}%{_datadir}/doc/man-db/* ./

# remove zsoelim man page - part of groff package
rm %{buildroot}%{_datadir}/man/man1/zsoelim.1

# install cache directory
install -d -m 0755  %{buildroot}%{_localstatedir}/cache/man

# config for tmpfiles.d
install -D -p -m 0644 init/systemd/man-db.conf %{buildroot}/usr/lib/tmpfiles.d/.

# One package have two lang files
%find_lang %{name}
%find_lang %{name}-gnulib

%pre
# remove alternativized files if they are not symlinks
for f in man apropos whatis; do
    [ -L %{_bindir}/$f ] || %{__rm} -f %{_bindir}/$f >/dev/null 2>&1 || :
    [ -L %{_mandir}/man1/$f.1.gz ] || %{__rm} -f %{_mandir}/man1/$f.1.gz >/dev/null 2>&1 || :
done

# stop and disable timer from previous builds
if [ -e /usr/lib/systemd/system/mandb.timer ]; then
    if test -d /run/systemd; then
        systemctl stop man-db.timer >/dev/null 2>&1 || :
        systemctl -q disable man-db.timer >/dev/null 2>&1 || :
    fi
fi
%post
# set up the alternatives files
%{_sbindir}/update-alternatives --install %{_bindir}/man man %{_bindir}/man.%{name} 300 \
    --slave %{_bindir}/apropos apropos %{_bindir}/apropos.%{name} \
    --slave %{_bindir}/whatis whatis %{_bindir}/whatis.%{name} \
    --slave %{_mandir}/man1/man.1.gz man.1.gz %{_mandir}/man1/man.%{name}.1.gz \
    --slave %{_mandir}/man1/apropos.1.gz apropos.1.gz %{_mandir}/man1/apropos.%{name}.1.gz \
    --slave %{_mandir}/man1/whatis.1.gz whatis.1.gz %{_mandir}/man1/whatis.%{name}.1.gz \
    >/dev/null 2>&1 || :

# clear the old cache
%{__rm} -rf %{cache}/* >/dev/null 2>&1 || :
%systemd_post man-db.service man-db.timer

%preun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove man %{_bindir}/man.%{name} >/dev/null 2>&1 || :
fi
%systemd_preun man-db.service man-db.timer

%postun
if [ $1 -ge 1 ]; then
    if [ "$(readlink %{_sysconfdir}/alternatives/man)" == "%{_bindir}/man.%{name}" ]; then
        %{_sbindir}/update-alternatives --set man %{_bindir}/man.%{name} >/dev/null 2>&1 || :
    fi
fi
%systemd_postun man-db.service man-db.timer

%check -p
export LANG=C

%files -f %{name}.lang -f %{name}-gnulib.lang
%license COPYING
%doc README.md man-db-manual.txt man-db-manual.ps ChangeLog NEWS.md
%config(noreplace) %{_sysconfdir}/man_db.conf
%config(noreplace) %{_tmpfilesdir}/man-db.conf
%{_sbindir}/accessdb
%ghost %{_bindir}/man
%ghost %{_bindir}/apropos
%ghost %{_bindir}/whatis
%{_bindir}/man.%{name}
%{_bindir}/apropos.%{name}
%{_bindir}/whatis.%{name}
%{_bindir}/man-recode
%{_bindir}/manpath
%{_bindir}/lexgrog
%{_bindir}/catman
%{_bindir}/mandb
%dir %{_libdir}/man-db
%{_libdir}/man-db/*.so
%dir %{_libexecdir}/man-db
%{_libexecdir}/man-db/globbing
%{_libexecdir}/man-db/manconv
%{_libexecdir}/man-db/zsoelim
%{_unitdir}/man-db.service
%{_unitdir}/man-db.timer
%verify(not mtime) %dir %{_localstatedir}/cache/man
%ghost %{_mandir}/man1/man.1*
%ghost %{_mandir}/man1/apropos.1*
%ghost %{_mandir}/man1/whatis.1*
%{_mandir}/man1/man.%{name}.1*
%{_mandir}/man1/apropos.%{name}.1*
%{_mandir}/man1/whatis.%{name}.1*
%{_mandir}/man1/man-recode.1*
%{_mandir}/man1/lexgrog.1*
%{_mandir}/man1/manconv.1*
%{_mandir}/man1/manpath.1*
%{_mandir}/man5/manpath.5*
%{_mandir}/man8/accessdb.8*
%{_mandir}/man8/catman.8*
%{_mandir}/man8/mandb.8*
%lang(it) %{_datadir}/man/it/man*/*

%changelog
%autochangelog

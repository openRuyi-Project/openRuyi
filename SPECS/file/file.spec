# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           file
Version:        5.46
Release:        %autorelease
Summary:        A Tool to Determine File Types
License:        BSD-2-Clause
URL:            http://www.darwinsys.com/file/
VCS:            git:https://github.com/file/file
#!RemoteAsset
Source0:        https://www.astron.com/pub/file/file-%{version}.tar.gz
#!RemoteAsset
Source1:        https://www.astron.com/pub/file/file-%{version}.tar.gz.asc
Buildsystem:    autotools

BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --enable-fsect-man5

BuildRequires:  bash
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  make

%description
With the file command, you can obtain information on the file type of a
specified file. File type recognition is controlled by the file
/etc/magic, which contains the classification criteria. This command is
used by apsfilter to permit automatic printing of different file types.

%package        devel
Summary:        Development files for libmagic, a library to determine file types
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glibc-devel

%description    devel
This package contains all necessary include files and libraries needed
to develop applications that require the magic "file" interface.

%conf -p
autoreconf -fiv

%files
%defattr (-,root,root)
%attr(755,root,root) %{_bindir}/file
%{_libdir}/lib*.so.*
%{_datadir}/misc/magic.mgc
%doc %{_mandir}/man1/file.1.gz
%license COPYING
%doc AUTHORS NEWS ChangeLog

%files devel
%defattr (-,root,root)
%{_libdir}/lib*.so
%{_includedir}/magic.h
%{_libdir}/pkgconfig/libmagic.pc
%doc %{_mandir}/man3/libmagic.3.gz
%defattr (-,root,root)
%doc %{_mandir}/man5/magic.5.gz
%license COPYING
%doc README.DEVELOPER AUTHORS NEWS ChangeLog

%changelog
%autochangelog

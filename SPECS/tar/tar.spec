# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tar
Version:        1.35
Release:        %autorelease
Summary:        GNU file archiving program
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/tar/tar.html
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
BuildSystem:    autotools

# Next release will fix this - 251
Patch0:         0001-tar-1.35-revert-fix-savannah-bug-633567.patch
# And this, too - 251
Patch1:         0002-add-forgotten-tests.patch

BuildRequires:  gettext
BuildRequires:  acl-devel
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  texinfo


%install -a
%find_lang %{name} --generate-subpackages

%description
The GNU tar program saves many files together in one archive and can
restore individual files (or all of the files) from that archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive. Tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives, and the ability to perform incremental and full
backups.

If you want to use tar for remote backups, you also need to install
the rmt package on the remote box.

%check
make %{?_smp_mflags} check || { cat tests/testsuite.log; exit 1; }

%files
%license COPYING
%doc AUTHORS README THANKS NEWS ChangeLog
%{_bindir}/tar
%{_libexecdir}/rmt
%{_mandir}/man1/tar.1*
%{_mandir}/man8/rmt.8*
%{_infodir}/tar.info*

%changelog
%{?autochangelog}

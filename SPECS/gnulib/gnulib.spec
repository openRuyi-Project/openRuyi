# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global githead 4e11e3d
%global gitdate 20260316

Name:           gnulib
Version:        0+git%{gitdate}.%{githead}
Release:        %autorelease
Summary:        GNU Portability Library
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND GFDL-1.3-or-later AND FSFULLRSD
URL:            https://www.gnu.org/software/gnulib
VCS:            git:https://git.savannah.gnu.org/git/gnulib.git
#!RemoteAsset
Source:         https://git.savannah.gnu.org/gitweb/?p=gnulib.git;a=snapshot;h=%{githead};sf=tgz;name=gnulib-%{githead}.tar.gz#/gnulib-%{githead}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  bison
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  help2man
BuildRequires:  git
BuildRequires:  pkgconfig(python3)

Requires:       libtool
Requires:       texinfo
Requires:       diffutils
Requires:       patch
Requires:       m4
Requires:       grep
Requires:       gawk
Requires:       help2man

%description
The GNU portability library is a macro system and C declarations and
definitions for commonly-used API elements and abstracted system behaviors.
It can be used to improve portability and other functionality in your programs.

%prep -a
toRemove="lib-symbol-visibility havelib .*-obsolete localcharset gettext-h gettext alloca-opt alloca "

list="$(./gnulib-tool --list)"
for item in $toRemove
do
   list="$(echo $list| sed "s:\b$item\b::g")"
done

# is necessary to avoid some modules to test prep pass
./gnulib-tool --create-testdir --with-tests --with-obsolete --avoid=alloca --avoid=lib-symbol-visibility --avoid=havelib --dir=build-tests $list

%conf -p
cd build-tests
# FIX ERROR CAN'T DETECT AC_LIB_PREPARE_PREFIX
mkdir m4
autoreconf -fiv -I%{_datadir}/gettext/m4
%configure --prefix=%_prefix

%build
pushd build-tests
make %{?_smp_mflags}
popd

sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/gnulib#" gnulib-tool
sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/gnulib#" gnulib-tool.sh
sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/gnulib#" gnulib-tool.py

# Removing unused files
rm -f */.cvsignore
rm -f */.gitignore
rm -f */.gitattributes
rm -f lib/.cppi-disable
rm -f lib/uniname/gen-uninames.lisp

%install
mkdir -p %{buildroot}%{_datadir}/gnulib
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/info
mkdir -p %{buildroot}%{_pkgdocdir}
mkdir -p %{buildroot}%{_mandir}/man1

cp -p check-module %{buildroot}%{_bindir}
cp -p gnulib-tool gnulib-tool.sh gnulib-tool.py %{buildroot}%{_datadir}/gnulib/
cp -rp build-aux lib m4 modules config tests %{buildroot}%{_datadir}/gnulib/
cp -p .gnulib-tool.py %{buildroot}%{_datadir}/gnulib/
mkdir -p %{buildroot}%{_datadir}/gnulib/doc
cp -p NEWS COPYING ChangeLog HACKING users.txt doc/COPYING* %{buildroot}%{_pkgdocdir}/
rm -f doc/COPYING*
cp -avr doc/* %{buildroot}/%{_datadir}/gnulib/doc/
cp -rp top %{buildroot}%{_datadir}/gnulib/

%check
make -C build-tests check VERBOSE=1

%files
%{_datadir}/gnulib/
%{_bindir}/check-module
%{_pkgdocdir}/

%changelog
%autochangelog

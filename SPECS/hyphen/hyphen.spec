# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           hyphen
Version:        2.8.8
Release:        %autorelease
Summary:        A text hyphenation library
License:        GPL-2.0-only OR LGPL-2.1-or-later OR MPL-1.1
URL:            http://hunspell.sf.net
VCS:            git:https://github.com/hunspell/hyphen
#!RemoteAsset
Source0:        https://sourceforge.net/projects/hunspell/files/Hyphen/2.8/hyphen-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Hyphen is a library for high quality hyphenation and justification.

%package        devel
Summary:        Files for developing with hyphen
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Includes and definitions for developing with hyphen.

%package        en
Summary:        English hyphenation rules
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    en
English hyphenation rules.

%install -a
pushd %{buildroot}%{_datadir}/hyphen/
en_US_aliases="en_AG en_AU en_BS en_BW en_BZ en_CA en_DK en_GB en_GH en_HK en_IE en_IN en_JM en_MW en_NA en_NZ en_PH en_SG en_TT en_ZA en_ZM en_ZW"
for lang in $en_US_aliases; do
        ln -s hyph_en_US.dic hyph_$lang.dic
done
popd

%files
%doc AUTHORS ChangeLog README README.hyphen README.nonstandard TODO
%{_libdir}/*.so.*
%dir %{_datadir}/hyphen

%files en
%{_datadir}/hyphen/hyph_en*.dic

%files devel
%{_includedir}/hyphen.h
%{_libdir}/*.so
%{_bindir}/substrings.pl

%changelog
%autochangelog

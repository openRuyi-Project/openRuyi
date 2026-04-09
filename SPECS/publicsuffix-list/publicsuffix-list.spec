# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           publicsuffix-list
Version:        20251008
Release:        %autorelease
Summary:        Cross-vendor public domain suffix database
License:        MPL-2.0
URL:            https://publicsuffix.org/
# VCS: No VCS link available
# https://publicsuffix.org/list/public_suffix_list.dat
Source0:        public_suffix_list.dat
# https://www.mozilla.org/media/MPL/2.0/index.txt
Source1:        index.txt
# https://github.com/publicsuffix/list/raw/main/tests/test_psl.txt
Source2:        test_psl.txt

%description
The Public Suffix List is a cross-vendor initiative to provide an accurate list
of domain name suffixes. Web clients use this list to restrict where cookies
may be set, protecting users from cross-site tracking.

%prep
%setup -c -T
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%install
install -d -m 755 %{buildroot}%{_datadir}/publicsuffix
install -m 644 -p public_suffix_list.dat %{buildroot}%{_datadir}/publicsuffix/
install -m 644 -p test_psl.txt %{buildroot}%{_datadir}/publicsuffix/
install -m 644 -p index.txt %{buildroot}%{_datadir}/publicsuffix/
ln -s public_suffix_list.dat %{buildroot}%{_datadir}/publicsuffix/effective_tld_names.dat

%files
%dir %{_datadir}/publicsuffix
%{_datadir}/publicsuffix/effective_tld_names.dat
%{_datadir}/publicsuffix/public_suffix_list.dat
%{_datadir}/publicsuffix/test_psl.txt
%{_datadir}/publicsuffix/index.txt

%changelog
%autochangelog

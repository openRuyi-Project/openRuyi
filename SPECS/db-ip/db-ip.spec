# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstream_version 2026-05

Name:           db-ip
Version:        2026.05
Release:        %autorelease
Summary:        DB-IP City Lite Database
License:        CC-BY-4.0
URL:            https://db-ip.com/
#!RemoteAsset:  sha256:9520cc8c65dc04cafc88682ac89dba2cfbbcb5f686e9094ab021fcf2ae2c02f0
Source0:        https://download.db-ip.com/free/dbip-city-lite-%{upstream_version}.mmdb.gz
#!RemoteAsset:  sha256:d781b1eb0d41cd2fb7fb1cfa0a227738c9b72a0bd4da97fecfd4ce8b2764cb85
Source1:        https://download.db-ip.com/free/dbip-asn-lite-%{upstream_version}.mmdb.gz
#!RemoteAsset:  sha256:9ba9550ad48438d0836ddab3da480b3b69ffa0aac7b7878b5a0039e7ab429411
Source2:        https://creativecommons.org/licenses/by/4.0/legalcode.txt
BuildArch:      noarch

%description
This package contains the free DB-IP City Lite database in MMDB format.
It provides IPv4 and IPv6 routing data with city-level geolocation.
This data is updated monthly by DB-IP.

%prep
%setup -c -T
gunzip -c %{SOURCE0} > dbip-city-lite.mmdb
gunzip -c %{SOURCE1} > dbip-asn-lite.mmdb
cp %{SOURCE2} LICENSE

%install
mkdir -p %{buildroot}%{_datadir}/db-ip
install -p -m 0644 dbip-city-lite.mmdb %{buildroot}%{_datadir}/db-ip/
install -p -m 0644 dbip-asn-lite.mmdb %{buildroot}%{_datadir}/db-ip/

%files
%license LICENSE
%dir %{_datadir}/db-ip
%{_datadir}/db-ip/dbip-city-lite.mmdb
%{_datadir}/db-ip/dbip-asn-lite.mmdb

%changelog
%autochangelog

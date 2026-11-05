# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global orbit_version 1.5.4.v200908052355
Name:           itext-birt
Version:        1.5.4
Release:        %autorelease
Summary:        iText PDF and font APIs for Eclipse BIRT
License:        MPL-1.1 AND MIT AND Apache-2.0 AND BSD-3-Clause-No-Nuclear-Warranty AND Unicode-DFS-2015 AND APAFML AND LicenseRef-iText-JavaWorld AND LicenseRef-iText-JavaSpecialists
URL:            https://www.eclipse.org/birt/
# VCS: No VCS link available
# This source bundle identifies its implementation as iText 1.5.2 for Eclipse/BIRT.
#!RemoteAsset:  sha256:45496738784643e817d1becc5d01b66a8a26abde1aaa46defe231b30c77535d9
Source0:        https://archive.eclipse.org/tools/orbit/downloads/drops/R20090825191606/updateSite/plugins/com.lowagie.text.source_%{orbit_version}.jar
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  unzip

%patchlist
# Downstream adaptation of the public ImageIO writer used by later iText versions.
# https://sources.debian.org/src/libitext-java/2.1.7-14/src/core/com/lowagie/text/pdf/PdfGraphics2D.java/
2000-use-imageio-for-pdf-graphics.patch

%description
This BIRT release of iText supplies the com.lowagie PDF writer, reader
and font metrics interfaces used by the Pentaho report engine.

%prep
%setup -q -c -T
unzip -q %{SOURCE0}
sed -i 's/\r$//' com/lowagie/text/pdf/PdfGraphics2D.java
%autopatch -p1

%build
mkdir classes
find com -name '*.java' | sort > sources.list
javac --release 8 -encoding ISO-8859-1 -d classes @sources.list
find com -type f ! -name '*.java' -exec cp --parents -p {} classes/ \;
jar --create --file itext-birt.jar -C classes .

%install
install -Dpm644 itext-birt.jar %{buildroot}%{_datadir}/java/itext-birt.jar

# The upstream source distribution does not include an automated test suite.

%files
%doc about.html
%license about_files/MPL-1.1.txt com/lowagie/bc/asn1/bouncycastle_license.txt
%license com/lowagie/text/apache_license.txt com/lowagie/text/misc_licenses.txt
%license com/lowagie/text/pdf/fonts/mustRead.html
%{_datadir}/java/itext-birt.jar

%changelog
%autochangelog

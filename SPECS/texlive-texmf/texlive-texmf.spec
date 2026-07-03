# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tl_year     2026
%global tl_snapshot 20260301

# Only used as metadata to find upstream command names in texlive.tlpdb.
%global tl_link_arch x86_64-linux

# Directories for both sources
%global tl_texmf_dir texlive-%{tl_snapshot}-texmf
%global tl_extra_dir texlive-%{tl_snapshot}-extra

# Shared rpm scriptlet body for TeX Live cache refreshes.  These operations are
# intentionally non-fatal so a cache/tool issue does not break rpm transactions.
%define texlive_refresh_caches() \
if [ -x %{_bindir}/mktexlsr ]; then %{_bindir}/mktexlsr >/dev/null 2>&1 || :; fi; \
if [ -x %{_bindir}/updmap-sys ]; then %{_bindir}/updmap-sys --nohash >/dev/null 2>&1 || :; fi; \
if [ -x %{_bindir}/fmtutil-sys ]; then %{_bindir}/fmtutil-sys --all >/dev/null 2>&1 || :; fi; \
if [ -x %{_bindir}/mtxrun ]; then %{_bindir}/mtxrun --generate >/dev/null 2>&1 || :; fi; \
:

Name:           texlive-texmf
Version:        %{tl_snapshot}
Release:        %autorelease
Summary:        TeX Live data
License:        Apache-2.0 AND Artistic-2.0 AND BSD-3-Clause AND GFDL-1.1-or-later AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND Knuth-CTAN AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND LPPL-1.3a AND LPPL-1.3c AND MIT AND OFL-1.1 AND LicenseRef-openRuyi-Public-Domain
URL:            https://tug.org/texlive/
VCS:            svn:https://tug.org/svn/texlive/trunk
# See https://tug.org/historic/
#!RemoteAsset:  sha256:349eb7c5c2c15333d77490a52934b053c6dcb88834f2224978f7a4edf67940e7
Source0:        https://mirror.nju.edu.cn/tex-historic/systems/texlive/%{tl_year}/texlive-%{tl_snapshot}-texmf.tar.xz
#!RemoteAsset:  sha256:68d78428d012bce8c2ffaf7027c701a66c51039a16059d33f30980330033a5d0
Source1:        https://mirror.nju.edu.cn/tex-historic/systems/texlive/%{tl_year}/texlive-%{tl_snapshot}-extra.tar.xz
Source2:        texlive-generate-split.py
Source3:        texlive-collections.txt
Source4:        texlive-script-aliases.txt
BuildArch:      noarch

BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  python3
BuildRequires:  sed

Requires:       texlive-meta = %{version}-%{release}

%description
TeX Live is a distribution of the TeX typesetting system.

This compatibility metapackage installs the main TeX Live collection
metapackage.

%package     -n texlive-doc
Summary:        Documentation for TeX Live

%description -n texlive-doc
This package contains the large TeX Live documentation tree, manual pages, and
GNU info pages.

%package     -n texlive-meta
Summary:        Metapackage to install TeX Live non-language collections
Requires:       texlive-basic = %{version}-%{release}
Requires:       texlive-bibtexextra = %{version}-%{release}
Requires:       texlive-binextra = %{version}-%{release}
Requires:       texlive-context = %{version}-%{release}
Requires:       texlive-fontsextra = %{version}-%{release}
Requires:       texlive-fontsrecommended = %{version}-%{release}
Requires:       texlive-fontutils = %{version}-%{release}
Requires:       texlive-formatsextra = %{version}-%{release}
Requires:       texlive-games = %{version}-%{release}
Requires:       texlive-humanities = %{version}-%{release}
Requires:       texlive-latex = %{version}-%{release}
Requires:       texlive-latexextra = %{version}-%{release}
Requires:       texlive-latexrecommended = %{version}-%{release}
Requires:       texlive-luatex = %{version}-%{release}
Requires:       texlive-mathscience = %{version}-%{release}
Requires:       texlive-metapost = %{version}-%{release}
Requires:       texlive-music = %{version}-%{release}
Requires:       texlive-pictures = %{version}-%{release}
Requires:       texlive-plaingeneric = %{version}-%{release}
Requires:       texlive-pstricks = %{version}-%{release}
Requires:       texlive-publishers = %{version}-%{release}
Requires:       texlive-xetex = %{version}-%{release}

%description -n texlive-meta
This metapackage installs the main non-language TeX Live collections.

Language collections remain optional.

%package     -n texlive-basic
Summary:        TeX Live collection: basic
Provides:       texlive-core = %{version}-%{release}
Obsoletes:      texlive-core < %{version}-%{release}
Requires:       perl
Requires:       texlive >= %{version}
Recommends:     biber

%description -n texlive-basic
This package contains the TeX Live basic collection.

%package     -n texlive-bibtexextra
Summary:        TeX Live collection: bibtexextra
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-bibtexextra
This package contains the TeX Live bibtexextra collection.

%package     -n texlive-binextra
Summary:        TeX Live collection: binextra
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}
Recommends:     python3
Recommends:     perl

%description -n texlive-binextra
This package contains the TeX Live binextra collection.

%package     -n texlive-context
Summary:        TeX Live collection: context
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-context
This package contains the TeX Live context collection.

%package     -n texlive-fontsextra
Summary:        TeX Live collection: fontsextra
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-fontsextra
This package contains the TeX Live fontsextra collection.

%package     -n texlive-fontsrecommended
Summary:        TeX Live collection: fontsrecommended
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-fontsrecommended
This package contains the TeX Live fontsrecommended collection.

%package     -n texlive-fontutils
Summary:        TeX Live collection: fontutils
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-fontutils
This package contains the TeX Live fontutils collection.

%package     -n texlive-formatsextra
Summary:        TeX Live collection: formatsextra
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}
Requires:       texlive-plaingeneric = %{version}-%{release}
Requires:       texlive-fontsrecommended = %{version}-%{release}
Requires:       texlive-latexrecommended = %{version}-%{release}

%description -n texlive-formatsextra
This package contains the TeX Live formatsextra collection.

%package     -n texlive-games
Summary:        TeX Live collection: games
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-games
This package contains the TeX Live games collection.

%package     -n texlive-humanities
Summary:        TeX Live collection: humanities
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-humanities
This package contains the TeX Live humanities collection.

%package     -n texlive-langarabic
Summary:        TeX Live collection: langarabic
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langarabic
This package contains the TeX Live langarabic collection.

%package     -n texlive-langchinese
Summary:        TeX Live collection: langchinese
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langchinese
This package contains the TeX Live langchinese collection.

%package     -n texlive-langcjk
Summary:        TeX Live collection: langcjk
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langcjk
This package contains the TeX Live langcjk collection.

%package     -n texlive-langcyrillic
Summary:        TeX Live collection: langcyrillic
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langcyrillic
This package contains the TeX Live langcyrillic collection.

%package     -n texlive-langczechslovak
Summary:        TeX Live collection: langczechslovak
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langczechslovak
This package contains the TeX Live langczechslovak collection.

%package     -n texlive-langenglish
Summary:        TeX Live collection: langenglish
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langenglish
This package contains the TeX Live langenglish collection.

%package     -n texlive-langeuropean
Summary:        TeX Live collection: langeuropean
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langeuropean
This package contains the TeX Live langeuropean collection.

%package     -n texlive-langfrench
Summary:        TeX Live collection: langfrench
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langfrench
This package contains the TeX Live langfrench collection.

%package     -n texlive-langgerman
Summary:        TeX Live collection: langgerman
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langgerman
This package contains the TeX Live langgerman collection.

%package     -n texlive-langgreek
Summary:        TeX Live collection: langgreek
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langgreek
This package contains the TeX Live langgreek collection.

%package     -n texlive-langitalian
Summary:        TeX Live collection: langitalian
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langitalian
This package contains the TeX Live langitalian collection.

%package     -n texlive-langjapanese
Summary:        TeX Live collection: langjapanese
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langjapanese
This package contains the TeX Live langjapanese collection.

%package     -n texlive-langkorean
Summary:        TeX Live collection: langkorean
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langkorean
This package contains the TeX Live langkorean collection.

%package     -n texlive-langpolish
Summary:        TeX Live collection: langpolish
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langpolish
This package contains the TeX Live langpolish collection.

%package     -n texlive-langportuguese
Summary:        TeX Live collection: langportuguese
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langportuguese
This package contains the TeX Live langportuguese collection.

%package     -n texlive-langspanish
Summary:        TeX Live collection: langspanish
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langspanish
This package contains the TeX Live langspanish collection.

%package     -n texlive-langother
Summary:        TeX Live collection: langother
Provides:       texlive-langextra = %{version}-%{release}
Obsoletes:      texlive-langextra < %{version}-%{release}
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-langother
This package contains the TeX Live langother collection.

%package     -n texlive-latex
Summary:        TeX Live collection: latex
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-latex
This package contains the TeX Live latex collection.

%package     -n texlive-latexextra
Summary:        TeX Live collection: latexextra
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-latexextra
This package contains the TeX Live latexextra collection.

%package     -n texlive-latexrecommended
Summary:        TeX Live collection: latexrecommended
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-latexrecommended
This package contains the TeX Live latexrecommended collection.

%package     -n texlive-luatex
Summary:        TeX Live collection: luatex
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-luatex
This package contains the TeX Live luatex collection.

%package     -n texlive-mathscience
Summary:        TeX Live collection: mathscience
Provides:       texlive-science = %{version}-%{release}
Obsoletes:      texlive-science < %{version}-%{release}
Requires:       texlive-basic = %{version}-%{release}
Requires:       texlive >= %{version}

%description -n texlive-mathscience
This package contains the TeX Live mathscience collection.

%package     -n texlive-metapost
Summary:        TeX Live collection: metapost
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-metapost
This package contains the TeX Live metapost collection.

%package     -n texlive-music
Summary:        TeX Live collection: music
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-music
This package contains the TeX Live music collection.

%package     -n texlive-pictures
Summary:        TeX Live collection: pictures
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-pictures
This package contains the TeX Live pictures collection.

%package     -n texlive-plaingeneric
Summary:        TeX Live collection: plaingeneric
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-plaingeneric
This package contains the TeX Live plaingeneric collection.

%package     -n texlive-pstricks
Summary:        TeX Live collection: pstricks
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-pstricks
This package contains the TeX Live pstricks collection.

%package     -n texlive-publishers
Summary:        TeX Live collection: publishers
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}

%description -n texlive-publishers
This package contains the TeX Live publishers collection.

%package     -n texlive-xetex
Summary:        TeX Live collection: xetex
Requires:       texlive >= %{version}
Requires:       texlive-basic = %{version}-%{release}
Requires:       texlive-latex = %{version}-%{release}

%description -n texlive-xetex
This package contains the TeX Live xetex collection.

%prep
%autosetup -c -T
tar -xf %{SOURCE0}
tar -xf %{SOURCE1}

%build
# No build is required for TeX Live data.

%install
install -d %{buildroot}%{_datadir}
cp -a %{tl_texmf_dir}/texmf-dist %{buildroot}%{_datadir}/texmf-dist
cp -a %{tl_extra_dir}/tlpkg %{buildroot}%{_datadir}/tlpkg

# Split the very large documentation tree into texlive-doc.
# Use find+mv rather than globbing so empty directories and
# dotfiles are handled predictably.
install -d %{buildroot}%{_docdir}/texlive
if [ -d %{buildroot}%{_datadir}/texmf-dist/doc ]; then
    find %{buildroot}%{_datadir}/texmf-dist/doc -mindepth 1 -maxdepth 1 \
        -exec mv -t %{buildroot}%{_docdir}/texlive {} +
    rmdir %{buildroot}%{_datadir}/texmf-dist/doc
    ln -s %{_docdir}/texlive %{buildroot}%{_datadir}/texmf-dist/doc
fi

if [ -d %{buildroot}%{_docdir}/texlive/info ]; then
    install -d %{buildroot}%{_infodir}
    find %{buildroot}%{_docdir}/texlive/info -mindepth 1 -maxdepth 1 \
        -exec mv -t %{buildroot}%{_infodir} {} +
    rmdir %{buildroot}%{_docdir}/texlive/info
fi

if [ -d %{buildroot}%{_docdir}/texlive/man ]; then
    install -d %{buildroot}%{_mandir}
    find %{buildroot}%{_docdir}/texlive/man -mindepth 1 -maxdepth 1 \
        -exec mv -t %{buildroot}%{_mandir} {} +
    rmdir %{buildroot}%{_docdir}/texlive/man
fi

# Strip executable bit from a bundled prebuilt helper in documentation.
# It is kept as documentation/example material, not shipped as a runnable program.
for f in %{_docdir}/texlive/optex/opbible/txs-gen/mod2tex; do
    test -e %{buildroot}$f || continue
    chmod 0644 %{buildroot}$f
done

# Basic distro integration files are owned by texlive-basic.
install -d %{buildroot}%{_datadir}/fontconfig/conf.avail
cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/09-texlive-fonts.conf << EOF
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">
<fontconfig>
    <dir>%{_datadir}/texmf-dist/fonts/opentype</dir>
    <dir>%{_datadir}/texmf-dist/fonts/truetype</dir>
    <dir>%{_datadir}/texmf-dist/fonts/type1</dir>
</fontconfig>
EOF

install -d %{buildroot}%{_sysconfdir}/fonts/conf.d
ln -s %{_datadir}/fontconfig/conf.avail/09-texlive-fonts.conf \
    %{buildroot}%{_sysconfdir}/fonts/conf.d/09-texlive-fonts.conf

# Use /etc/texmf as the authoritative location for local configuration.
# Keep the upstream texmf-dist paths as symlinks to avoid two independent
# copies of texmf.cnf/fmtutil/updmap/language configuration.
install -d %{buildroot}%{_sysconfdir}/texmf/web2c
for cfg in texmf.cnf fmtutil.cnf updmap.cfg mktex.cnf; do
    src=%{buildroot}%{_datadir}/texmf-dist/web2c/$cfg
    if [ -f "$src" ]; then
        install -m 0644 "$src" %{buildroot}%{_sysconfdir}/texmf/web2c/$cfg
        rm -f "$src"
        ln -s ../../../../etc/texmf/web2c/$cfg "$src"
    fi
done

install -d %{buildroot}%{_sysconfdir}/texmf/tex/generic/config
for lang_cfg in language.dat language.dat.lua language.def; do
    src=%{buildroot}%{_datadir}/texmf-dist/tex/generic/config/$lang_cfg
    if [ -f "$src" ]; then
        install -m 0644 "$src" %{buildroot}%{_sysconfdir}/texmf/tex/generic/config/$lang_cfg
        rm -f "$src"
        ln -s ../../../../../../etc/texmf/tex/generic/config/$lang_cfg "$src"
    fi
done

if [ -f %{buildroot}%{_sysconfdir}/texmf/web2c/texmf.cnf ]; then
    sed -i \
        -e 's|^TEXMFROOT = .*|TEXMFROOT = %{_datadir}|' \
        -e 's|^TEXMFSYSVAR = .*|TEXMFSYSVAR = %{_sharedstatedir}/texmf|' \
        -e 's|^TEXMFSYSCONFIG = .*|TEXMFSYSCONFIG = %{_sysconfdir}/texmf|' \
        %{buildroot}%{_sysconfdir}/texmf/web2c/texmf.cnf
fi
install -d %{buildroot}%{_sharedstatedir}/texmf/arch/installedpkgs

# Generate collection file lists from tlpkg/texlive.tlpdb.
# The script expands ordinary TeX Live package dependencies recursively, assigns
# files to one owning collection, and emits diagnostics for files that had to be
# assigned by the final fallback.
rm -rf %{_builddir}/texlive-generated
install -d %{_builddir}/texlive-generated

python3 %{SOURCE2} \
    --buildroot %{buildroot} \
    --tlpdb %{buildroot}%{_datadir}/tlpkg/texlive.tlpdb \
    --texmf-dist %{buildroot}%{_datadir}/texmf-dist \
    --collections %{SOURCE3} \
    --script-aliases %{SOURCE4} \
    --tl-link-arch %{tl_link_arch} \
    --datadir %{_datadir} \
    --bindir %{_bindir} \
    --sharedstatedir %{_sharedstatedir} \
    --sysconfdir %{_sysconfdir} \
    --docdir %{_docdir}/texlive \
    --mandir %{_mandir} \
    --infodir %{_infodir} \
    --outdir %{_builddir}/texlive-generated

%check
# No upstream test suite is associated with the data tarballs.

%transfiletriggerin -n texlive-basic -- %{_datadir}/texmf-dist %{_sysconfdir}/texmf %{_datadir}/tlpkg %{_sharedstatedir}/texmf/arch/installedpkgs
%texlive_refresh_caches

%transfiletriggerpostun -n texlive-basic -- %{_datadir}/texmf-dist %{_sysconfdir}/texmf %{_datadir}/tlpkg %{_sharedstatedir}/texmf/arch/installedpkgs
%texlive_refresh_caches

%files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-meta
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-doc -f %{_builddir}/texlive-generated/texlive-doc.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-basic -f %{_builddir}/texlive-generated/texlive-basic.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-bibtexextra -f %{_builddir}/texlive-generated/texlive-bibtexextra.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-binextra -f %{_builddir}/texlive-generated/texlive-binextra.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-context -f %{_builddir}/texlive-generated/texlive-context.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-fontsextra -f %{_builddir}/texlive-generated/texlive-fontsextra.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-fontsrecommended -f %{_builddir}/texlive-generated/texlive-fontsrecommended.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-fontutils -f %{_builddir}/texlive-generated/texlive-fontutils.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-formatsextra -f %{_builddir}/texlive-generated/texlive-formatsextra.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-games -f %{_builddir}/texlive-generated/texlive-games.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-humanities -f %{_builddir}/texlive-generated/texlive-humanities.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langarabic -f %{_builddir}/texlive-generated/texlive-langarabic.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langchinese -f %{_builddir}/texlive-generated/texlive-langchinese.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langcjk -f %{_builddir}/texlive-generated/texlive-langcjk.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langcyrillic -f %{_builddir}/texlive-generated/texlive-langcyrillic.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langczechslovak -f %{_builddir}/texlive-generated/texlive-langczechslovak.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langenglish -f %{_builddir}/texlive-generated/texlive-langenglish.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langeuropean -f %{_builddir}/texlive-generated/texlive-langeuropean.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langfrench -f %{_builddir}/texlive-generated/texlive-langfrench.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langgerman -f %{_builddir}/texlive-generated/texlive-langgerman.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langgreek -f %{_builddir}/texlive-generated/texlive-langgreek.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langitalian -f %{_builddir}/texlive-generated/texlive-langitalian.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langjapanese -f %{_builddir}/texlive-generated/texlive-langjapanese.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langkorean -f %{_builddir}/texlive-generated/texlive-langkorean.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langother -f %{_builddir}/texlive-generated/texlive-langother.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langpolish -f %{_builddir}/texlive-generated/texlive-langpolish.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langportuguese -f %{_builddir}/texlive-generated/texlive-langportuguese.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-langspanish -f %{_builddir}/texlive-generated/texlive-langspanish.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-latex -f %{_builddir}/texlive-generated/texlive-latex.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-latexextra -f %{_builddir}/texlive-generated/texlive-latexextra.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-latexrecommended -f %{_builddir}/texlive-generated/texlive-latexrecommended.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-luatex -f %{_builddir}/texlive-generated/texlive-luatex.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-mathscience -f %{_builddir}/texlive-generated/texlive-mathscience.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-metapost -f %{_builddir}/texlive-generated/texlive-metapost.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-music -f %{_builddir}/texlive-generated/texlive-music.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-pictures -f %{_builddir}/texlive-generated/texlive-pictures.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-plaingeneric -f %{_builddir}/texlive-generated/texlive-plaingeneric.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-pstricks -f %{_builddir}/texlive-generated/texlive-pstricks.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-publishers -f %{_builddir}/texlive-generated/texlive-publishers.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%files -n texlive-xetex -f %{_builddir}/texlive-generated/texlive-xetex.files
%license %{tl_extra_dir}/LICENSE.TL %{tl_extra_dir}/LICENSE.CTAN

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# This package (and all subpackages) are intentionally empty meta-packages.
# Disable automatic debuginfo/debugsource generation to avoid build failures
# due to missing debugfiles.list.
%global debug_package %{nil}

Name:           langpacks
Version:        1.0
Release:        %autorelease
Summary:        Language meta-package
License:        MIT
# URL: No URL link available
# VCS: No VCS link available

%description
This is a meta-package to provide language packages.

%package        be
Summary:        Language meta-package (Belarusian)

%description    be
This is a meta-package for language "Belarusian".

%package        bg
Summary:        Language meta-package (Bulgarian)

%description    bg
This is a meta-package for language "Bulgarian".

%package        ca
Summary:        Language meta-package (Catalan)

%description    ca
This is a meta-package for language "Catalan".

%package        cs
Summary:        Language meta-package (Czech)

%description    cs
This is a meta-package for language "Czech".

%package        da
Summary:        Language meta-package (Danish)

%description    da
This is a meta-package for language "Danish".

%package        de
Summary:        Language meta-package (German)

%description    de
This is a meta-package for language "German".

%package        el
Summary:        Language meta-package (Greek)

%description    el
This is a meta-package for language "Greek".

%package        eo
Summary:        Language meta-package (Esperanto)

%description    eo
This is a meta-package for language "Esperanto".

%package        es
Summary:        Language meta-package (Spanish)

%description    es
This is a meta-package for language "Spanish".

%package        fi
Summary:        Language meta-package (Finnish)

%description    fi
This is a meta-package for language "Finnish".

%package        fr
Summary:        Language meta-package (French)

%description    fr
This is a meta-package for language "French".

%package        hr
Summary:        Language meta-package (Croatian)

%description    hr
This is a meta-package for language "Croatian".

%package        hu
Summary:        Language meta-package (Hungarian)

%description    hu
This is a meta-package for language "Hungarian".

%package        ia
Summary:        Language meta-package (Interlingua)

%description    ia
This is a meta-package for language "Interlingua".

%package        id
Summary:        Language meta-package (Indonesian)

%description    id
This is a meta-package for language "Indonesian".

%package        it
Summary:        Language meta-package (Italian)

%description    it
This is a meta-package for language "Italian".

%package        ja
Summary:        Language meta-package (Japanese)

%description    ja
This is a meta-package for language "Japanese".

%package        ka
Summary:        Language meta-package (Georgian)

%description    ka
This is a meta-package for language "Georgian".

%package        ko
Summary:        Language meta-package (Korean)

%description    ko
This is a meta-package for language "Korean".

%package        lt
Summary:        Language meta-package (Lithuanian)

%description    lt
This is a meta-package for language "Lithuanian".

%package        nb
Summary:        Language meta-package (Norwegian Bokmål)

%description    nb
This is a meta-package for language "Norwegian Bokmål".

%package        nl
Summary:        Language meta-package (Dutch)

%description    nl
This is a meta-package for language "Dutch".

%package        pl
Summary:        Language meta-package (Polish)

%description    pl
This is a meta-package for language "Polish".

%package        pt
Summary:        Language meta-package (Portuguese)

%description    pt
This is a meta-package for language "Portuguese".

%package        ro
Summary:        Language meta-package (Romanian)

%description    ro
This is a meta-package for language "Romanian".

%package        ru
Summary:        Language meta-package (Russian)

%description    ru
This is a meta-package for language "Russian".

%package        rw
Summary:        Language meta-package (Kinyarwanda)

%description    rw
This is a meta-package for language "Kinyarwanda".

%package        sk
Summary:        Language meta-package (Slovak)

%description    sk
This is a meta-package for language "Slovak".

%package        sl
Summary:        Language meta-package (Slovenian)

%description    sl
This is a meta-package for language "Slovenian".

%package        sr
Summary:        Language meta-package (Serbian)

%description    sr
This is a meta-package for language "Serbian".

%package        sv
Summary:        Language meta-package (Swedish)

%description    sv
This is a meta-package for language "Swedish".

%package        tr
Summary:        Language meta-package (Turkish)

%description    tr
This is a meta-package for language "Turkish".

%package        uk
Summary:        Language meta-package (Ukrainian)

%description    uk
This is a meta-package for language "Ukrainian".

%package        vi
Summary:        Language meta-package (Vietnamese)

%description    vi
This is a meta-package for language "Vietnamese".

%package        zh
Summary:        Language meta-package (Chinese)

%description    zh
This is a meta-package for language "Chinese".

%files

%files be

%files bg

%files ca

%files cs

%files da

%files de

%files el

%files eo

%files es

%files fi

%files fr

%files hr

%files hu

%files ia

%files id

%files it

%files ja

%files ka

%files ko

%files lt

%files nb

%files nl

%files pl

%files pt

%files ro

%files ru

%files rw

%files sk

%files sl

%files sr

%files sv

%files tr

%files uk

%files vi

%files zh

%changelog
%autochangelog

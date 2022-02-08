backimg =[
  'https://img.muspace.top/img/E0.webp',
  'https://img.muspace.top/img/A2.webp',
  'https://img.muspace.top/img/A80.webp',
  'https://img.muspace.top/img/A88.webp',
  'https://img.muspace.top/img/A285.webp',
  'https://img.muspace.top/img/735.webp',
  'https://img.muspace.top/img/A319.webp',
  'https://img.muspace.top/img/590.webp',
  'https://img.muspace.top/img/506.webp',
  'https://img.muspace.top/img/46.webp',
  'https://img.muspace.top/img/362.webp',
  'https://img.muspace.top/img/318.webp',
  'https://img.muspace.top/img/145.webp',
  'https://img.muspace.top/img/D2.webp',
  'https://img.muspace.top/img/D1.webp',
  'https://img.muspace.top/img/D0.webp',
  'https://img.muspace.top/img/B0.webp',
  'https://img.muspace.top/img/H18.webp',
  'https://img.muspace.top/img/H1.webp',
  'https://img.muspace.top/img/H2.webp',
  'https://img.muspace.top/img/H7.webp',
  'https://img.muspace.top/img/I0.webp',
  'https://img.muspace.top/img/I6.webp',
  'https://img.muspace.top/img/I17.webp',
  'https://img.muspace.top/img/I60.webp',
  'https://img.muspace.top/img/H4.webp',
  'https://img.muspace.top/img/I13.webp',
  'https://img.muspace.top/img/I62.webp',
  'https://img.muspace.top/img/I193.webp',
  'https://img.muspace.top/img/I234.webp',
  'https://img.muspace.top/img/H12.webp',
  'https://img.muspace.top/img/I147.webp',
  'https://img.muspace.top/img/I231.webp',
  'https://img.muspace.top/img/J010.webp',
  'https://img.muspace.top/img/J10.webp',
  'https://img.muspace.top/img/J75.webp',
  'https://img.muspace.top/img/J22.webp',
  'https://img.muspace.top/img/J40.webp',
  'https://img.muspace.top/img/91810456.webp',
  'https://img.muspace.top/img/wallhaven-dgv23j.webp',
  'https://img.muspace.top/img/J4.webp',
  'https://img.muspace.top/img/J62.web'
]

def main(lists,to_path):
    import os,shutil
    paths=[]
    for a in lists:
        path=a.split('https://img.muspace.top/')[1].split(')')[0]
        paths.append(path)
    for path in paths:
        shutil.copy(path,to_path)
        os.remove(path)

main(backimg,'Cover')
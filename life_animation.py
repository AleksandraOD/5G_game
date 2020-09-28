import matplotlib.pyplot as plt
import matplotlib.animation as animation
import life_process as lp
import argparse


def create_life(
        field_size,
        start_seed,
        start_seed_point,
        quality,
        interval,
        n_generations,
        cmap,
        save,
        filename

):
    """
    Create game animation

    :param field_size: tuple ()
    :param start_seed: str (name for the seed array)
    :param start_seed_point: str (tuple of integers representing the start seed position)
    :param quality: int (resolution of the animation)
    :param interval: int (delay between frames)
    :param n_generations: int (number of frames/ duration of animation)
    :param cmap: str (color scheme name)
    :param save: bool (flag to toggle saving of the animation)
    :param filename: str (filename for output gif)
    """
    field = lp.seeded_field(field_size, start_seed, start_seed_point)

    fig = plt.figure(dpi=quality, figsize=plt.figaspect(field))
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
    plt.axis("off")
    ims = []

    for i in range(n_generations):
        field = lp.generation(field)
        ims.append((plt.imshow(field, cmap=cmap),))

    field_animation = animation.ArtistAnimation(fig, ims, blit=True, interval=interval, repeat=False)

    if save:
        field_animation.save((str(filename) + ".gif"), writer='pillow')
    plt.close()

    return field_animation


if __name__ == "__main__":

    # collect command line arguments or display help context
    parser = argparse.ArgumentParser(description="Game of life")

    parser.add_argument("--cmap",
                        type=str,
                        default="autumn",
                        help="Color scheme, in double quotes: \"Greens\". Defaults to autumn.")

    parser.add_argument("--filename",
                        type=str,
                        default="life",
                        help="Desired filename, if --save = True. Defaults to life.")

    parser.add_argument("--interval",
                        type=int,
                        default=50,
                        help="Delay between frames. Defaults to 50.")

    parser.add_argument("--n-generations",
                        type=int,
                        default=25,
                        help="Number of generations. Defaults to 25.")

    parser.add_argument("--quality",
                        type=int,
                        default=100,
                        help="Image quality. Defaults to 100.")

    parser.add_argument("--save",
                        type=bool,
                        default=True,
                        help="Save animation: True or False. Defaults to True.")

    parser.add_argument("--start-seed",
                        type=str,
                        default="infinite",
                        help="Starting seed, in double quotes. Try \"glider\" or \"block\"; check out the "
                             "README for full list of seeds. Defaults to infinite")

    parser.add_argument("--start-seed-point",
                        type=str,
                        default="-1,-1",
                        help="Starting seed x,y position, in double quotes. Defaults to the center of the field.")

    parser.add_argument("--field-size",
                        type=str,
                        default="100,100",
                        help="Size of the field, in double quotes: \"width,height\". Defaults to 100 x 100.")

    args = parser.parse_args()

    create_life(
        field_size=(
            int(args.field_size.split(',')[0]),
            int(args.field_size.split(',')[1])
        ),
        start_seed=args.start_seed,
        start_seed_point=(
            int(args.start_seed_point.split(',')[0]),
            int(args.start_seed_point.split(',')[1])
        ),
        quality=args.quality,
        interval=args.interval,
        n_generations=args.n_generations,
        cmap=args.cmap,
        save=args.save,
        filename=args.filename
    )
